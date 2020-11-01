import sys 


def main(word):
    asciiElem = [ord(ele) for sub in word for ele in sub]
    binElem = []
    for elem in asciiElem:
        letterBin = bin(elem)[2:]
        letterBin += str(letterBin.count('1')%2)
        binElem.append(letterBin)
    bcc = ""
    for i in range(0, len(binElem[0])):
        countOne = 0
        for elem in binElem:
            if elem[i] == '1':
                countOne += 1
        bcc += str(countOne%2)
    binElem.append(bcc)
    print(binElem)




data  = sys.argv
word = data[1]
main(word)