from qiskit import QuantumCircuit
import numpy as np

def test():
    state = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    norm = np.linalg.norm(state)
    normalized_state = state / norm
    num_qubits = 4
    circ = QuantumCircuit(num_qubits)
    circ.initialize(normalized_state, [0, 1, 2, 3])
    print(circ.decompose(reps = 8))
    

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

if __name__ == "__main__":
    test()
    # angleEncoderZ(1)
    # angleEncoderZZ(1)
