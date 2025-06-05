import numpy as np
import math as m
from numpy import random

# take user input for cores, qubits per core, qubits, gates, probabilities, and file name
def getUserInput():
    # read and extract parameters from architecture.txt
    arch = open("samples/architecture.txt", "r")
    read_arch = arch.readlines()
    mesh_x = int(read_arch[0].strip("mesh_x "))
    mesh_y = int(read_arch[1].strip("mesh_y "))

    number_of_cores = mesh_x * mesh_y
    qubits_per_core = int(read_arch[3].strip("qubits_per_core "))
    number_of_qubits = qubits_per_core * number_of_cores
    number_of_gates = int(input("Number of gates: "))

    usable_qubits = number_of_qubits # initializes variable for while loop

    # qcomm simulator seems to only simulate less than 80% of the total qubits declared
    overhead = m.ceil(0.8 * number_of_qubits)
    while usable_qubits >= overhead:
        usable_qubits = int(input(f"Number of logical qubits (must be <80% or <{overhead} qubits): "))

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

    return(number_of_cores, qubits_per_core, number_of_qubits, number_of_gates, usable_qubits, probabilities, file_name, mesh_x, mesh_y) # returns tuple

def adjacentCore(i, width, length):
    noc_array = []
    count = width # helper variable
    
    # creates 2D array of cores in sequential order in rows then columns
    for y in range(length):
        noc_array.append([])
        x = count - width
        while x < count:
            noc_array[y].append(x)
            x += 1
        count += width

    row_number = 0 # track row index

    # determines the coordinate of the core
    for row in noc_array:
        column_number = 0 # track column index
        for column in row:
            if column == i:
                source_coord = [row_number, column_number]
                break
            column_number += 1
        row_number += 1

    # determines destination (adjacent) coordinate
    while True:
        destination_coord = source_coord.copy() # so that when modifying destination coordinate it doesn't point to the source coordinate

        # randomly generates addition or subtraction operation to column or row number of source coordinate
        add_or_subtract = random.randint(0, 2)
        row_or_column = random.randint(0, 2)
        
        if add_or_subtract == 0:
            # add to row number
            if row_or_column == 0:
                destination_coord[0] += 1
            # add to column number
            if row_or_column == 1:
                destination_coord[1] += 1

        if add_or_subtract == 1:
            # subtract to row number
            if row_or_column == 0:
                destination_coord[0] -= 1
            # substract to column number
            if row_or_column == 1:
                destination_coord[1] -= 1

        # breaks the loop if the generated coordinates is within bounds of the array
        if 0 <= destination_coord[0] < len(noc_array) and 0 <= destination_coord[1] < len(noc_array[0]):
            break
    
    j = noc_array[destination_coord[0]][destination_coord[1]]

    return j

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
    x = user_input[7]
    y = user_input[8]

    # number of bits to perform bit reversal on depends on the amount of cores
    bits = m.log(cores, 2)
    bits = m.ceil(bits)

    gate_list = intToList(len(probs)) # convert number of gates to list of n-qubit gates

    random_size_gate_list = random.choice(gate_list, p = probs, size = (gates)).tolist() # list of 1, 2 ... n-qubit gates; probability of each; size of final list which is total amount of gates

    with open(f"samples/bit_reversal/{file}", "w") as test_circuit:
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

        for gate in random_size_gate_list:
            string = "("

            track_gate = [] # tracks qubits within a gate

            # bit reversal if 2-qubit gate
            if gate == 2:
                source_qubit = random.randint(usable)
                corresponding_core = findCore(mapper, source_qubit)


                adjacent_core = adjacentCore(corresponding_core, x, y)

                # makes sure qubits are not repeated within the same 2-qubit gate
                while True:
                    destination_qubit = np.random.choice(mapper[adjacent_core])
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

            # if a qubit is repeated then create a new line before the current gate
            if repeating:
                index = string.rfind("(")
                string = string[:index] + "\n(" + string[index + 1:]

                # reset qubit tracker and current slice
                current_slice = []

            test_circuit.write(string)

if __name__ == "__main__":
    generator()