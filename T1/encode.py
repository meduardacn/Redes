from nrzi import NRZI
from mdif import MDIF
from hdb3 import HDB3
from eightb6t import EightB6T
from sixb8b import SixB8B
import sys 

def main(technique, binary, hexa):
    if technique == "nrzi":
        NRZI.encode(binary)
    elif technique == "mdif":
        MDIF.encode(binary)
    elif technique == "hdb3":
        HDB3.encode(binary)
    elif technique == "8b6t":
        EightB6T.encode(hexa)
    elif technique == "6b8b":
        SixB8B.encode(binary)


data  = sys.argv
hexaLen = len(data[2])
binary = bin(int(data[2], 16))
binary = binary[2:] + ""
while len(binary) < hexaLen*4:
    binary = "0" + binary

main(data[1],binary,data[2])