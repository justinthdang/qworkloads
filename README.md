# How to Use Qcomm
Qcomm is a C++ simulation framework for quantum circuit communication and mapping. It reads a quantum circuit, architecture configuration, and simulation parameters, and runs a simulation to collect statistics.

All core functionality, architecture, and simulation logic of this repository was created by the original authors of Qcomm. The original repository can be found [here](https://github.com/mpalesi/qcomm).

This cloned repository simply fixes some missing headers, reorganizes the C++ files into a src folder, and provides clear instructions on how to get the tool up and running.

If you use this tool in academic work, please consider citing the original authors and publications associated with QComm.

## Rebuilding Simulator
To rebuild the simulator, navigate to the project directory and execute the following:
#### `make clean`
#### `make`

## Customizing the Circuit, Architecture, and Parameters
A list of inputs for the circuit, architecture, and parameters text files can be found under section III of [this paper](https://arxiv.org/pdf/2405.16275).

An example can be found in the "samples" folder within the project directory.

## Running the Simulator
To run the simulator, navigate to the project directory and execute the following:
#### `./qcomm -c samples/circuit.txt -a samples/architecture.txt -p samples/parameters.txt`

## Citations
Maurizio Palesi, Enrico Russo, Davide Patti, Giuseppe Ascia, and Vincenzo Catania, "_Assessing the Role of Communication in Scalable Multi-Core Quantum Architectures_," in _2024 IEEE 17th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC)_, Kuala Lumpur, Malaysia, 2024, pp. 482-489, doi: 10.1109/MCSoC64144.2024.00085.
