import qiskit
from qiskit.circuit.library import ZZFeatureMap, ZFeatureMap

# angle encoder following Qiskit's ZFeatureMap circuit implementation
def angleEncoderZ(reps):
    # workload_list = select_nodes(input_size, network, circuit_file)
    workload_list = [0, 16, 32, 48, 64, 80, 96, 4, 20, 36, 52, 68, 84, 100, 5, 21] # e.g., cores 0, 4, and 5
    circuit = ""
    slices = 2 * reps

    for slice in range(slices):
        for i in workload_list:
            circuit += f"({i}) "
        circuit += "\n"

    print(circuit)

# angle encoder following Qiskit's ZZFeatureMap circuit implementation (linear entanglement)
def angleEncoderZZ(reps):
    # workload_list = select_nodes(input_size, network, circuit_file)
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

    print(circuit)

if __name__ == "__main__":
    angleEncoderZ(2)
    angleEncoderZZ(2)