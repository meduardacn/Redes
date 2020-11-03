import sys 
def encode(binaryLetter, binaryGenerator):
    letterSlice = binaryLetter[:len(binaryGenerator)] # Pega os 5 primeiros bits
    i = len(binaryGenerator) # índice de quanto do binário ja foi verificado
    zeros = "0"*len(binaryGenerator) # lista de zeros
    xorResult = 0
    while i <= len(binaryLetter): 
        if letterSlice[0] == "1": # verifica primeiro bit
            xorResult = int(letterSlice, 2) ^ int(binaryGenerator,2) # xor com binário
        else: 
            xorResult = int(letterSlice, 2) ^ int(zeros, 2) # cor com 0's
        letterSlice = '{0:b}'.format(xorResult) # transforma resultado do xor em binário
        while len(letterSlice) != len(binaryGenerator): # adiciona 0's a esquerda
            letterSlice = "0" + letterSlice
        if i != len(binaryLetter):
            letterSlice = letterSlice[1:] + binaryLetter[i] # remove primeiro bit e adiciona um índice no final 
        i+=1 # atualiza indíce
    result = binaryLetter[:len(binaryLetter)-len(binaryGenerator)+1] + letterSlice[1:] # retira 0's e adiciona o resultado final do xor
    result =  hex(int(result, 2))[2:] #transforma em hexa
    return(result.upper())

def main(word,binaryGenerator):
    result = ""
    binLetter = ""
    for elem in [ord(ele) for sub in word for ele in sub]: # tranforma letra em código ASCII
        binLetter = bin(elem)[2:]         # transforma código ASCII em binário
        binLetter += "0"*(len(data[2])-1)  # adiciona zeros
        result += encode(binLetter,binaryGenerator) # concatena encode de cada letra
    print(result)

data  = sys.argv
if len(data[2]) == 5: # verifica se o binário gerador tem tamanho 5
    main(data[1],data[2])
else:
    print("ERRO")
