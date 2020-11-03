import sys 


def main(word):
    asciiElem = [ord(ele) for sub in word for ele in sub] # cria a lista de códico ascii
    binElem = []
    for elem in asciiElem: 
        letterBin = bin(elem)[2:] # remove 0b
        letterBin += str(letterBin.count('1')%2) # conta a quantidade de 1, e usa módulo para adicionar bit de paridade
        binElem.append(letterBin) # adiciona código binário
    bcc = ""
    for i in range(0, len(binElem[0])): # percorre indice dos binários
        countOne = 0
        for elem in binElem: # para cada binário
            if elem[i] == '1': 
                countOne += 1
        bcc += str(countOne%2) # adiciona bit para binário de paridade
    binElem.append(bcc) # adiona binário de paridade
    result = ""
    for elem in binElem:
        result +=  hex(int(elem, 2))[2:] # transforma cada binário em hexa
    print(result.upper())




data  = sys.argv
word = data[1] # palavra
main(word)