import sys 
def decode(letter, binaryGenerator):
    binaryLetter = bin(int(letter, 16))[2:]
    letterSlice = binaryLetter[:len(binaryGenerator)]
    i = len(binaryGenerator)
    zeros = "0"*len(binaryGenerator)
    xorResult = 0
    while i <= len(binaryLetter):
        if letterSlice[0] == "1":
            xorResult = int(letterSlice, 2) ^ int(binaryGenerator, 2)
        else:
            xorResult = int(letterSlice, 2) ^ int(zeros, 2)
        letterSlice = '{0:b}'.format(xorResult)
        while len(letterSlice) != len(binaryGenerator):
            letterSlice = "0" + letterSlice
        if i != len(binaryLetter):
            letterSlice = letterSlice[1:] + binaryLetter[i]
        i += 1
    result = letterSlice[1:]
    result = hex(int(result, 2))[2:]
    if int(result) != 0:
        return "_"
    else:
        return(chr(int(bin(int(letter[:-1], 16))[2:], 2)))
        
def main(hexa,generator):
    result = ""
    for i in range(0, int(len(hexa)/3)):
        letter = hexa[i*3:(i+1)*3]
        response = decode(letter,generator)
        result += response
    print(result)
    errors = []
    for i in range(len(result)):
        if result[i] == "_":
            errors.append(i+1)
    if errors != []:
        print("ERRO nos caracteres:",errors)
data  = sys.argv
main(data[1],data[2])
