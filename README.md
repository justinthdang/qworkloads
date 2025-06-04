# Qcomm Circuit Generator
This repository adds working random circuit generator scripts for 1- and 2-qubit gates of various synthetic NoC traffic patterns to be simulated with in Qcomm. These implementations fix the issues with the ### `./rcg` command in Qcomm, which generates circuits that cause the simulation to abort, all while expanding the range of circuits that could be simulated for research purposes.

Additionally, this repository fixes some missing headers from the [original Qcomm repository](https://github.com/mpalesi/qcomm) so that the simulation could run.

All core functionality, architecture, and simulation logic of this repository was created by the original authors of Qcomm. If you use this tool in academic work, please consider citing the original authors and publications associated with Qcomm.

## Rebuilding Simulator
To rebuild the simulator, navigate to the project directory and execute the following:
#### `make clean`
#### `make`

## Customizing the Circuit, Architecture, and Parameters
To generate a random circuit, navigate to the traffic folder and run the script with your desired traffic pattern in your IDE. The script reads the amount of cores, qubits per core, and hence, qubits, defined in the architecture.txt file within the samples folder. It also prompts for the amount of gates desired, the probabilities of each n-qubit gate, the amount of usable qubits (typically below 80% to avoid multi-core communication conflicts), and a .txt file to write the generated circuit into.

A list of inputs for the architecture.txt and parameters.txt files can be found under section III of [this paper](https://arxiv.org/pdf/2405.16275).

## Running the Simulator
To run the simulator, execute the following:
#### `./qcomm -c <path to circuit text file> -a <path to architecture text file> -p <path to parameters text file>`

## Citations
Maurizio Palesi, Enrico Russo, Davide Patti, Giuseppe Ascia, and Vincenzo Catania, "_Assessing the Role of Communication in Scalable Multi-Core Quantum Architectures_," in _2024 IEEE 17th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC)_, Kuala Lumpur, Malaysia, 2024, pp. 482-489, doi: 10.1109/MCSoC64144.2024.00085.
