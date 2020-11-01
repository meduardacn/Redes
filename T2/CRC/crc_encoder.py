import sys 

def main(binaryWord, binaryGenerator):
    wordSlice = binaryWord[:len(binaryGenerator)]
    i = len(binaryGenerator)
    zeros = "0"*len(binaryGenerator)
    xorResult = 0
    while i < len(binaryWord):
        if wordSlice[0] == "1":
            xorResult = int(wordSlice, 2) ^ int(binaryGenerator,2)
        else: 
            xorResult = int(wordSlice, 2) ^ int(zeros, 2)
        wordSlice = '{0:b}'.format(xorResult)
        while len(wordSlice) != len(binaryGenerator):
            wordSlice = "0" + wordSlice
        wordSlice = wordSlice[1:] + binaryWord[i]
        i+=1
    print(binaryWord, "word")
    print(wordSlice, "resto final")
    result = binaryWord[:len(binaryWord)-len(binaryGenerator)+1] + wordSlice[1:]
    result =  hex(int(result, 2))[2:]
    print(result.upper())


data  = sys.argv
word = ""
for elem in [ord(ele) for sub in data[1] for ele in sub]:
    word += bin(elem)[2:]       # transform each letter into binary 
word += "0"*(len(data[2])-1)    # add zeros to the messege final
main(word,data[2])