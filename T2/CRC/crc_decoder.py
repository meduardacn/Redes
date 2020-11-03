import sys 
def decode(letter, binaryGenerator):
    binaryLetter = bin(int(letter, 16))[2:] #transforma hexa em bin
    letterSlice = binaryLetter[:len(binaryGenerator)] # Pega os 5 primeiros bits
    i = len(binaryGenerator) # índice de quanto do binário ja foi verificado
    zeros = "0"*len(binaryGenerator)# lista de zeros
    xorResult = 0
    while i <= len(binaryLetter):
        if letterSlice[0] == "1":# verifica primeiro bit
            xorResult = int(letterSlice, 2) ^ int(binaryGenerator, 2) # xor com binário
        else:
            xorResult = int(letterSlice, 2) ^ int(zeros, 2)# cor com 0's
        letterSlice = '{0:b}'.format(xorResult) # transforma resultado do xor em binário
        while len(letterSlice) != len(binaryGenerator):# adiciona 0's a esquerda
            letterSlice = "0" + letterSlice
        if i != len(binaryLetter):
            letterSlice = letterSlice[1:] + binaryLetter[i]# remove primeiro bit e adiciona um índice no final 
        i += 1 # atualiza indíce
    result = letterSlice[1:] # tira o primeiro bit o resultado do xor
    result = hex(int(result, 2))[2:] # transforma em hexa
    if int(result) != 0:
        return "_" # em caso de erro
    else:
        return(chr(int(bin(int(letter[:-1], 16))[2:], 2))) #transforma em char
        
def main(hexa,generator):
    result = ""
    for i in range(0, int(len(hexa)/3)): #percore a lista de hexa, dividinvo em n partes de 3 bits
        letter = hexa[i*3:(i+1)*3] # recebe 3 digitos
        response = decode(letter,generator)
        result += response # concatena decode de cada letra
    print(result)
    errors = []
    for i in range(len(result)):
        if result[i] == "_": # verifica se a letra esta errada
            errors.append(i+1)
    if errors != []: # informa que teve erros
        print("ERRO nos caracteres:",errors)
data  = sys.argv
if len(data[2]) == 5:# verifica se o binário gerador tem tamanho 5
    main(data[1], data[2])
else:
    print("ERRO")

