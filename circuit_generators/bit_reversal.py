import numpy as np
import math as m
from numpy import random

# take user input for cores, qubits per core, qubits, gates, probabilities, and file name
def getUserInput():
    # read and extract parameters from architecture.txt
    arch = open("architecture.txt", "r")
    read_arch = arch.readlines()
    mesh_x = int(read_arch[0].strip("mesh_x "))
    mesh_y = int(read_arch[1].strip("mesh_y "))

    number_of_cores = mesh_x * mesh_y
    qubits_per_core = int(read_arch[3].strip("qubits_per_core "))
    number_of_qubits = qubits_per_core * number_of_cores
    number_of_gates = int(input("Number of gates: "))

    usable_qubits = number_of_qubits # initializes variable for while loop

    while usable_qubits >= number_of_qubits:
        usable_qubits = int(input(f"Number of logical qubits (must be <{number_of_qubits} qubits): "))

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

    # ask user for the name of the file the generated circuit will be outputted on
    file_name = ""
    while ".txt" not in file_name:
        file_name = input("Test circuit file name (include .txt): ")

    return(number_of_cores, qubits_per_core, number_of_qubits, number_of_gates, usable_qubits, probabilities, file_name) # returns tuple

def bitReverse(i, b):
    j = "" # initialize reversed string
    original = format(i, f"0{b}b") # convert from decimal to binary with specified bit string length

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

def findCore(dictionary, desired_value):
    for key, number in dictionary.items():
        if desired_value in number:
            return key

def generator():
    user_input = getUserInput()
    cores = user_input[0]
    qpc = user_input[1]
    qubits = user_input[2]
    gates = user_input[3]
    usable = user_input[4]
    probs = user_input[5]
    file = user_input[6]
    
    # number of bits to perform bit reversal on depends on the amount of cores
    bits = m.log(cores, 2)
    bits = m.ceil(bits)

    gate_list = intToList(len(probs)) # convert number of gates to list of n-qubit gates

    random_size_gate_list = np.random.choice(gate_list, p = probs, size = (gates)).tolist() # list of 1, 2 ... n-qubit gates; probability of each; size of final list which is total amount of gates

    with open(file, "w") as test_circuit:
        mapper = {} # maps qubits to cores
        qubit_list = [] # list for qubits in current core

        for core in range(cores):
            mod = core

            # adds qubits to a list in a certain multiple that satisfies the qubits per core
            while mod < usable:
                qubit_list.append(mod)
                mod += int(qubits / qpc)
            
            # map and reset for next set of qubits
            mapper[core] = qubit_list
            qubit_list = []

        current_slice = [] # tracks qubits used in current time slice

        gate_index = 0

        for gate in random_size_gate_list:
            string = "("

            track_gate = [] # tracks qubits within a gate

            # bit reversal if 2-qubit gate
            if gate == 2:
                source_qubit = random.randint(usable)
                corresponding_core = findCore(mapper, source_qubit)

                reversed_core = bitReverse(corresponding_core, bits)

                # makes sure qubits are not repeated within the same 2-qubit gate
                while True:
                    destination_qubit = np.random.choice(mapper[reversed_core])
                    if destination_qubit != source_qubit:
                        break
                
                current_slice.append(source_qubit)
                current_slice.append(destination_qubit)
                string += f"{source_qubit} {destination_qubit} "
            
            else:
                # generates random qubit within specified size of gate
                for i in range(1, gate + 1):
                    def rng(n, qrand, q):
                        # makes sure all numbers within a single gate are random
                        while True:
                            number = random.randint(n)
                            if number not in qrand:
                                qrand.append(number)
                                q.append(number)
                                return number
                
                    # generate qubit and add to gate
                    generated_qubit = rng(usable, track_gate, current_slice)
                    string += f"{generated_qubit} "

            string = string[:-1] + ") "

            # check if any numbers have been repeated
            repeating = [element for element in set(current_slice) if current_slice.count(element) > 1]

            # new line if qubit is repeating or the random number generated is greater than 0.5
            if repeating or (random.random() > 0.5 and gate_index != 0):
                index = string.rfind("(")
                string = string[:index] + "\n(" + string[index + 1:]

                # reset qubit tracker and current slice
                current_slice = []

            gate_index += 1
            test_circuit.write(string)

if __name__ == "__main__":
    generator()