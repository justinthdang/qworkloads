# angle encoder following Qiskit's ZFeatureMap circuit implementation
def angleEncoderZ(input_size, reps):
    circuit = ""
    slices = 2 * reps

    for slice in range(slices):
        for i in range(input_size):
            circuit += f"({i}) "
        circuit += "\n"

    print(circuit)

# angle encoder following Qiskit's ZZFeatureMap circuit implementation
def angleEncoderZZ(input_size, reps):
    circuit = ""
    
    for rep in range(reps):
        for slice in range(2):
            for i in range(input_size):
                circuit += f"({i}) "
            circuit += "\n"

        for slice in range(input_size - 1):
            circuit += f"({slice + 2} {slice + 1}) \n"
            circuit += f"({slice + 2}) \n"
            circuit += f"({slice + 2} {slice + 1}) \n"

    print(circuit)

if __name__ == "__main__":
    angleEncoderZ(16, 2)
    angleEncoderZZ(3, 2)