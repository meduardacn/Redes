import sys 

def main(binary):
    n = int(len(binary)/8) # binário de cada letra + binário de paridade
    binElem = []
    for i in range(0,n):
        elem = binary[i*8:(i+1)*8] #pega o i binário
        binElem.append(elem) # cria lista com binários separados

    for i in range(0, len(binElem[0])): # para todos os índices
        countOne = 0
        for elem in binElem[:-1]: # todos binários, exceto o de paridade
            if elem[i] == '1':
                countOne += 1
        if str(countOne%2) != binElem[-1][i]: # verifica se o bit do binário de paridade esta correto
            print("ERRO")
            return
    resultWord = ""
    for elem in binElem[:-1]: # todos binários, exceto o de paridade
        letterBin = elem[:-1] # recebe o  binário sem o último bit
        letterBin += str(letterBin.count('1')%2) # paridade dos 7 primeiros bit's
        if elem != letterBin: # verifica se o bit de paridade está errado
            print("ERRO")
            return
        else:
            resultWord += chr(int(elem[:-1],2)) # transforma binário em letra
    print(resultWord)


data  = sys.argv
binWord = bin(int(data[1], 16))[2:] #Transforma  hexa em binário
main(binWord)