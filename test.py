import subprocess
from circuit_generators.bit_reversal import gen1
from circuit_generators.neighbour import gen2

'''
def test():
    cmd = ["./qcomm", "-a", "architecture.txt", "-p", "parameters.txt", "-c", "samples/bit_reversal/5050circuit.txt"]
    with open("test.txt", "w") as outfile:
        subprocess.run(cmd, stdout=outfile, stderr=subprocess.STDOUT)
'''

def testamus():
    bit_reversal = gen1
    neighbour = gen2
    generators = [gen1, gen2]

    for i in generators:
        i()

if __name__ == "__main__":
    # test()
    testamus()
