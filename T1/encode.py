from nrzi import NRZI
from mdif import MDIF
from hdb3 import HDB3
from eightb6t import EightB6T
from sixb8b import SixB8B
import sys 

def main(technique, hexa):
    if technique == "nrzi":
        NRZI.encode(hexa)
    elif technique == "mdif":
        MDIF.encode(hexa)
    elif technique == "hdb3":
        HDB3.encode(hexa)
    elif technique == "8b6t":
        EightB6T.encode(hexa)
    elif technique == "6b8b":
        SixB8B.encode(hexa)


data  = sys.argv
print(data)
main(data[1],data[2])