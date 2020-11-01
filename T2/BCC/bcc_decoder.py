import sys 

def main(binary):
    n = int(len(binary)/8)
    binElem = []
    for i in range(0,n):
        elem = binary[i*8:(i+1)*8]
        binElem.append(elem)

    for i in range(0, len(binElem[0])):
        countOne = 0
        for elem in binElem[:-1]:
            if elem[i] == '1':
                countOne += 1
        if str(countOne%2) != binElem[-1][i]:
            print("ERRO")
            return
    resultWord = ""
    for elem in binElem[:-1]:
        letterBin = elem[:-1]
        letterBin += str(letterBin.count('1')%2)
        if elem != letterBin:
            print("ERRO")
            return
        else:
            resultWord += chr(int(elem[:-1],2))
    print(resultWord)


data  = sys.argv
binWord = bin(int(data[1], 16))[2:]
main(binWord)