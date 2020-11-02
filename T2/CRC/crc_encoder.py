import sys 
def encode(binaryLetter, binaryGenerator):
    letterSlice = binaryLetter[:len(binaryGenerator)]
    i = len(binaryGenerator)
    zeros = "0"*len(binaryGenerator)
    xorResult = 0
    while i <= len(binaryLetter):
        if letterSlice[0] == "1":
            xorResult = int(letterSlice, 2) ^ int(binaryGenerator,2)
        else: 
            xorResult = int(letterSlice, 2) ^ int(zeros, 2)
        letterSlice = '{0:b}'.format(xorResult)
        while len(letterSlice) != len(binaryGenerator):
            letterSlice = "0" + letterSlice
        if i != len(binaryLetter):
            letterSlice = letterSlice[1:] + binaryLetter[i]
        i+=1
    result = binaryLetter[:len(binaryLetter)-len(binaryGenerator)+1] + letterSlice[1:]
    result =  hex(int(result, 2))[2:]
    return(result.upper())

def main(word,binaryGenerator):
    result = ""
    binLetter = ""
    for elem in [ord(ele) for sub in word for ele in sub]:
        binLetter = bin(elem)[2:]         # transform letter into binary 
        binLetter += "0"*(len(data[2])-1)  # add zeros 
        result += encode(binLetter,binaryGenerator)
    print(result)

data  = sys.argv
if len(data[2]) == 5:
    main(data[1],data[2])
else:
    print("ERRO")
