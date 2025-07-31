# Qcomm Circuit Generator
This repository showcases the scripts I developed as part of my Summer 2025 undergraduate research assistantship on quantum computing. These scripts generate Qcomm-compatible circuit files for simulating synthetic traffic and neural network workloads on multi-core quantum architectures.

The scripts include uniform, bit-reversal, and neighbour traffics, as well as an encoder for neural workloads like Quantum Convolutional Neural Networks (QCNN) and Quantum Autoencoders (QAE). I have also written a .txt to .csv script to convert the simulation outputs of these circuits into organized tables for data visualization and analysis.

The full collection and rest of these generators can be accessed from [this joint research repository](https://github.com/Sadit-J/Qcomm-Traffic) maintained with my fellow research peers. Feel free to check out the results and findings from our research through [this paper]() we produced (currently in progress)!

All core functionality, architecture, and simulation logic of this repository was created by the original authors of Qcomm. If you use this tool in academic work, please consider citing the original authors and publications associated with Qcomm.

## Generating and Simulating Circuits
To generate a circuit, run the desired script found under the circuit_generators folder. This will output a .txt file of the circuit.

To simulate this circuit, please first refer to the installation and quick start guide from the [Qcomm repository](https://github.com/mpalesi/qcomm). Once Qcomm is set up, the files can be copied into this repository to begin simulating.

## Converting Circuit Simulation Data From .txt to .csv
Simulate the circuits of variable parameters in sequential order (e.g., 1 LTM port, 2 LTM ports, ..., n LTM ports). txt_to_csv.py essentially reads the simulation data file and splits each circuit simulation into a list element. For each table of a single variable parameter, the user will be prompted a title for the parameter, and the start and end indexes of it in the list.

The program will continue to loop for more tables until the user presses the enter key when prompted a title for the parameter. The first column of the generated tables will contain the name of the variable parameter (e.g, LTM ports), while the following columns will contain the corresponding statistics (e.g., communication time, coherence, etc.,).

An example of how a single generated table would look like:

| LTM Ports | Communication Time | ... | Coherence |
|-----------|--------------------|-----|-----------|
| 1         | 1e-2               | ... | 3e-4      |
| 2         | 5e-6               | ... | 7e-8      |
| ...       | ...                | ... | ...       |
| n         | 9e-1               | ... | 2e-3      |

## Citations
Maurizio Palesi, Enrico Russo, Davide Patti, Giuseppe Ascia, and Vincenzo Catania, "_Assessing the Role of Communication in Scalable Multi-Core Quantum Architectures_," in _2024 IEEE 17th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC)_, Kuala Lumpur, Malaysia, 2024, pp. 482-489, doi: 10.1109/MCSoC64144.2024.00085.
