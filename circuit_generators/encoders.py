from qiskit import QuantumCircuit
from qiskit.qasm2 import dumps
from qiskit.circuit.library import z_feature_map, zz_feature_map
import subprocess

# test function to generate amplitude encoder in Qiskit
def angleEncoder(nodes, repetitions, type):
    if type.lower() == "z":
        feature_map = z_feature_map(nodes, reps = repetitions)
    elif type.lower() == "zz":
        feature_map = zz_feature_map(nodes, reps = repetitions)

    node_list = []

    # must assign
    node_list = list(range(nodes))

    bound_circuit = feature_map.assign_parameters(node_list)

    qasm_circuit = dumps(bound_circuit)

    with open("encoder_circuit.qasm", "w") as f:
        f.write(qasm_circuit)

    cmd = ["python", "qasm2qcomm.py", "encoder_circuit.qasm"]
    result = subprocess.run(cmd, capture_output = True, text = True, check = True)

    encoder_circuit = result.stdout.rstrip()
    print(encoder_circuit)

if __name__ == "__main__":
    angleEncoder(16, 1, "z")


'''
# angle encoder following Qiskit's ZFeatureMap circuit implementation
def angleEncoderZ(reps):
    workload_list = [0, 16, 32, 48, 64, 80, 96, 4, 20, 36, 52, 68, 84, 100, 5, 21] # e.g., cores 0, 4, and 5
    circuit = ""
    slices = 2 * reps

    for slice in range(slices):
        for i in workload_list:
            circuit += f"({i}) "
        circuit += "\n"

    with open("ZFeatureMap.txt", "w") as f:
        f.write(circuit)
    print(circuit)

# angle encoder following Qiskit's ZZFeatureMap circuit implementation (linear entanglement)
def angleEncoderZZ(reps):
    workload_list = [0, 16, 32, 48, 64, 80, 96, 4, 20, 36, 52, 68, 84, 100, 5, 21] # e.g., cores 0, 4, and 5
    circuit = ""
    
    for rep in range(reps):

        for slice in range(2):
            for i in workload_list:
                circuit += f"({i}) "
            circuit += "\n"

        for i in range(len(workload_list) - 1):
            current_qubit = workload_list[i]
            next_qubit = workload_list[i + 1]
            circuit += f"({next_qubit} {current_qubit}) \n"
            circuit += f"({next_qubit}) \n"
            circuit += f"({next_qubit} {current_qubit}) \n"

    with open("ZZFeatureMap.txt", "w") as f:
        f.write(circuit)
    print(circuit)
'''