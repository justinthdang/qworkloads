# take user input for qubits, gates, probabilities
def getUserInput():
    number_of_qubits = int(input("Number of qubits: "))
    number_of_gates = int(input("Number of gates: "))

    probabilities = [] # initialize list for storing probabilities
    total_prob = 0 # initialize total probability
    n = 1 # initialize count for n-qubits
    
    # loops until total probability equals 1
    while total_prob != 1:
        n_qubit_gate_prob = float(input(f"{n}-qubit gate probability: "))

        total_prob += n_qubit_gate_prob # increment counter

        if not (0 <= n_qubit_gate_prob <= 1):
            print(f"{n}-qubit gate probability must be less between or equal to 0 and 1.")
            return
        
        probabilities.append(n_qubit_gate_prob) # add probability to list

    return(probabilities)

def main():
    return getUserInput()

if __name__ == "__main__":
    main()