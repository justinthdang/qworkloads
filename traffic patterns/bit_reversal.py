from numpy import random

# take user input for qubits, gates, probabilities
def getUserInput():
    # read and extract parameters from architecture.txt
    arch = open("samples/architecture.txt", "r")
    read_arch = arch.readlines()
    print(read_arch)
    mesh_x = read_arch[0].strip("mesh_x ")
    mesh_y = read_arch[1].strip("mesh_y ")

    number_of_cores = int(mesh_x) * int(mesh_y)
    qubits_per_core = int(read_arch[3].strip("qubits_per_core "))
    number_of_qubits = qubits_per_core * number_of_cores
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

    return(number_of_cores, qubits_per_core, number_of_qubits, number_of_gates, probabilities) # returns tuple

def bitReverse(i):
    j = "" # initialize reversed string
    original = bin(i).replace("0b", "") # convert decimal to binary
    # iterate through digits in reverse and add to reversed string
    for digit in reversed(original):
        j += digit
    reverse = int(j, 2) # convert binary to decimal
    return reverse

def intToList(i):
    my_list = []
    for number in range(1, i + 1):
        my_list.append(number)
    return my_list

def generator():
    user_input = getUserInput()
    n_cores = user_input[0]
    qpc = user_input[1]
    n_qubits = user_input[2]
    n_gates = user_input[3]
    probs = user_input[4]

    # convert number of gates to list of integers
    gate_list = intToList(n_gates)


    
    x = random.choice(gate_list, p = probs, size = (n_gates))
    

def main():
    user_input = getUserInput()
    print(user_input)
    # tingamus = bitReverse(8)
    # print(tingamus)

if __name__ == "__main__":
    main()