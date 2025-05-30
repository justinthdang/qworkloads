import random

# take user input for qubits, gates, probabilities
def getUserInput():
    number_of_qubits = int(input("Number of qubits: "))
    number_of_gates = int(input("Number of gates: "))

    probabilities = [] # initialize list for storing probabilities
    total_prob = 0 # initialize total probability tracker
    n = 1 # initialize count for n-qubits
    
    # loops until total probability equals 1 or the number probabilities exceeds the number of gates
    while total_prob != 1 and n <= number_of_gates:
        n_qubit_gate_prob = float(input(f"{n}-qubit gate probability: "))

        if not (0 <= n_qubit_gate_prob <= 1):
            print(f"{n}-qubit gate probability must be less between or equal to 0 and 1.")
            return
        
        # increment
        total_prob += n_qubit_gate_prob
        n += 1
        
        if total_prob > 1:
            print("Total probability must be 0 or 1.")
            return
        
        probabilities.append(n_qubit_gate_prob) # add probability to list

    return(number_of_qubits, number_of_gates,probabilities) # returns tuple

def bitReverse(i):
    j = "" # initialize reversed string
    original = bin(i).replace("0b", "") # convert decimal to binary
    # iterate through digits in reverse and add to reversed string
    for digit in reversed(original):
        j += digit
    reverse = int(j, 2) # convert binary to decimal
    return reverse

def generator():
    user_input = getUserInput()
    n_qubits = user_input[0]
    n_gates = user_input[1]
    probs = user_input[2]
    
    # n-qubits are 0, 1, 2 ... qubit states available, these could repeat so this determines when a slice ends
    # n-gates are 0-, 1-, 2- ... qubit gates available, this will be the determining factor of when the amount of slices end
    random.randrange(0, )

def main():
    # user_input = getUserInput()
    # print(user_input)
    tingamus = bitReverse(8)
    print(tingamus)

if __name__ == "__main__":
    main()