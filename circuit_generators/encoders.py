from qiskit import QuantumCircuit
from qiskit.qasm2 import dumps
from qiskit.circuit.library import z_feature_map
import subprocess

# test function to generate amplitude encoder in Qiskit
def angleEncoder(qubit_list, repetitions, entanglement_type, scaling_factor):
    qubits = len(qubit_list)
    feature_map = z_feature_map(qubits, reps = repetitions, entanglement = entanglement_type, alpha = scaling_factor)

    bound_circuit = feature_map.assign_parameters(qubit_list)
    qasm_circuit = dumps(bound_circuit)

    with open("encoder_circuit.qasm", "w") as f:
        f.write(qasm_circuit)

    cmd = ["python", "qasm2qcomm.py", "encoder_circuit.qasm"]
    result = subprocess.run(cmd, capture_output = True, text = True, check = True)

    encoder_circuit = result.stdout.rstrip()

    for i, qubit in enumerate(qubit_list):
        if f"({i})" in encoder_circuit:
            encoder_circuit = encoder_circuit.replace(f"({i})", f"({qubit}!")
    
    encoder_circuit = encoder_circuit.replace("!", ")")
    print(encoder_circuit)

if __name__ == "__main__":
    angleEncoder([0, 16, 32, 48, 64, 80, 96, 7, 23, 39, 55, 71, 87, 6, 22, 38, 54, 70, 86, 9, 25, 41, 57, 73, 89], 1, "full", 2.0)