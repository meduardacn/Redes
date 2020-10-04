from nrzi import NRZI
from mdif import MDIF
from hdb3 import HDB3
from eightb6t import EightB6T
from sixb8b import SixB8B
import sys 

def main(technique, sinal):
    if technique == "nrzi":
        result = NRZI.decode(sinal)
        print(result)
    elif technique == "mdif":
        MDIF.decode(sinal)
    elif technique == "hdb3":
        HDB3.decode(sinal)
    elif technique == "8b6t":
        EightB6T.decode(sinal)
    elif technique == "6b8b":
        SixB8B.decode(sinal)


data  = sys.argv
main(data[1],data[2])