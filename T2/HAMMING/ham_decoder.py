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
    
    onesPositions = []
    for i in range(0, len(binaryLetter)):       # find all places that have 1
        if binaryLetter[i] == '1':
            onesPositions.append(i+1)           
    
    xorResult = onesPositions[0] ^ onesPositions[1] # make xor between all positions that have one
    for i in range(2,len(onesPositions)):
        xorResult = xorResult ^ onesPositions[i]
    xorResult = bin(xorResult)[2:]

    if int(xorResult) == 0:          # without any bit error
        i, letter = 0, ""
        while i < len(binaryLetter): # clean letter, deleted hamming code
            i += 1
            if not isPowerOfTwo(i):
                letter += binaryLetter[i-1]
        letter = letter[::-1]         
        letter = chr(int(letter, 2))
        print(letter)
    return ""


def main(hexa):
    result = ""
    for i in range(0, int(len(hexa)/3)):
        letter = hexa[i*3:(i+1)*3]
        response = decode(letter)
        result += response
    print(result)
data = sys.argv
main(data[1])
