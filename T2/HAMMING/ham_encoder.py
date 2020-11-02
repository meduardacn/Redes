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
def encode(letter):
    asciiElem = ord(letter)                    # ascii => int
    binWord = bin(asciiElem)[2:]               # int => binary
    binWord = binWord[::-1]                    # reverse binary word
   
    i, hammingSpots , hammingWord = 0, 0, ""    
    while i-hammingSpots < len(binWord):       # find places to add hamming spots
        i += 1
        if isPowerOfTwo(i):
            hammingWord+= "_"
            hammingSpots += 1
        else:
            hammingWord += binWord[i-hammingSpots-1]
    onesPositions = []
    for i in range(0, len(hammingWord)):        # find all places that have 1
        if hammingWord[i] == '1':
            onesPositions.append(i+1)           # add one to the position
    onesPositions.reverse()

    xorResult = onesPositions[0] ^ onesPositions[1] # make xor between all positions that have one
    for i in range(2,len(onesPositions)):
        xorResult = xorResult ^ onesPositions[i]
    xorResult = bin(xorResult)[2:]

    while len(xorResult) < hammingSpots:        # normalize binary
        xorResult = '0'+xorResult
    xorResult = xorResult[::-1]

    j = 0
    resultMessage = "" 
    for i in range(0, len(hammingWord)):    # fill in the hamming word with the xor result
        if hammingWord[i] == '_':
            resultMessage += xorResult[j]
            j+= 1
        else:
            resultMessage += hammingWord[i]

    resultMessage = resultMessage[::-1]     # the reverse message of result binary
    return(hex(int(resultMessage, 2))[2:].upper())

def main(word):
    result = ""
    for elem in word:
        result+= encode(elem)
    print(result)
data = sys.argv
main(data[1])

