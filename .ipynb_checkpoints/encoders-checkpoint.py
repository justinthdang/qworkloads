import qiskit
from qiskit.circuit.library import ZZFeatureMap

def test():
    prep = ZZFeatureMap(3, reps=2)

    print(prep.decompose())

# angle encoder following Qiskit's ZFeatureMap circuit implementation
def angleEncoderZ(input_size, reps):
    size = input_size * input_size
    circuit = ""
    slices = 2 * reps

    for slice in range(slices):
        for i in range(size):
            circuit += f"({i}) "
        circuit += "\n"

    print(circuit)

# angle encoder following Qiskit's ZZFeatureMap circuit implementation
def angleEncoderZZ(input_size, reps):
    size = input_size * input_size
    circuit = ""
    
    for rep in range(reps):
        for slice in range(2):
            for i in range(size):
                circuit += f"({i}) "
            circuit += "\n"

        for slice in range(size - 1):
            circuit += f"({slice + 2} {slice + 1}) \n"
            circuit += f"({slice + 2}) \n"
            circuit += f"({slice + 2} {slice + 1}) \n"

    print(circuit)

def basisEncoder(input_size, reps):
    pass

# each pixel in an image has a vector (R, G, B)
# this means we need upwards of 255 qubits

if __name__ == "__main__":
    # angleEncoderZ(16, 2)
    # angleEncoderZZ(3, 2)
    test()