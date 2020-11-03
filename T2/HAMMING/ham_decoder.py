import sys
import math
def Log2(x):
    if x == 0:
        return False
    return (math.log10(x) /
            math.log10(2))

def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)))

def decode(letter):
    binaryLetter = bin(int(letter, 16))[2:] # hexa => bin
    binaryLetter = binaryLetter[::-1]       # reverse binary word

    # find all places that have '1'
    onesPositions = []
    for i in range(0, len(binaryLetter)):       
        if binaryLetter[i] == '1':
            onesPositions.append(i+1)           
    
    # make xor between all positions that have one
    xorResult = onesPositions[0] ^ onesPositions[1] 
    for i in range(2,len(onesPositions)):
        xorResult = xorResult ^ onesPositions[i]
    xorResult = bin(xorResult)[2:]
    
    # verify if have a  bit error and fix it
    error = 0
    if int(xorResult,2) != 0:          
        error = int(xorResult,2)
        if binaryLetter[error-1] == '1':
            binaryLetter = binaryLetter[:error-1]+'0'+ binaryLetter[error:]
        else:
            binaryLetter = binaryLetter[:error-1]+'1'+ binaryLetter[error:]
    
    # clean  binary letter deleting hamming code
    i, letter = 0, ""
    while i < len(binaryLetter): 
        i += 1
        if not isPowerOfTwo(i):
            letter += str(binaryLetter[i-1])

    # binary to char
    letter = letter[::-1]         
    letter = chr(int(letter,2))
    return (letter, error)

def main(hexa):
    result = ""
    errors = []
    for i in range(0, int(len(hexa)/3)):
        letter = hexa[i*3:(i+1)*3]
        response, error = decode(letter)
        errors.append(error)
        result += response
    print(result)
    for i in range(len(errors)):
        if errors[i] != 0:
            print("ERRO no caractere ", i+1 ," -> Correção: ", result[i])

data = sys.argv
main(data[1])