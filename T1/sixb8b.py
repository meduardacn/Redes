from nrzi import NRZI

class SixB8B():
    def table():
        f = open("sixb8b.txt", "r")
        text = f.read()
        text = text.split("\n")
        table = dict()
        for elem in text:
            value = elem.split(" ")
            table[value[0]] = value[1]
        return(table)

    def invertedTable():
        f = open("sixb8b.txt", "r")
        text = f.read()
        text = text.split("\n")
        table = dict()
        for elem in text:
            value = elem.split(" ")
            table[value[1]] = value[0]
        return(table)

    def encode(binary):
        i = 0
        n = int(len(binary)/6)
        table = SixB8B.table()
        result = ''
        for i in range(0,n):
            key = binary[i*6:(i+1)*6]
            ones = key.count('1')
            zeros = key.count('0')
            disparity = ones - zeros
            if disparity == 0:
                result += "10" + key 
            elif disparity == -2:
                result += "11" + key
            elif disparity == 2:
                result += "00" + key
            else:
                try:
                    result += table[key]
                except:
                    print('ERRO')
        NRZI.encode(result)

    def decode(sinal):
        i = 0
        n = int(len(sinal)/8)
        table = SixB8B.invertedTable()
        hexa = NRZI.decode(sinal)
        decode = hexaToBin(hexa)
        result = ''
        for i in range(0,n):
            key = decode[i*8:(i+1)*8]
            ones = key[2:].count('1')
            zeros = key[2:].count('0')
            disparity = ones - zeros
            if key[0:2] == '10' and disparity == 0:
                result += key[2:]
            elif key[0:2] == '11' and disparity == -2:
                result += key[2:]
            elif key[0:2] == '00' and disparity == 2:
                result += key[2:]
            else:
                try:
                    result += table[key]
                except:
                    print('ERRO')
                    return
        result = hex(int(result, 2))[2:] 
        print(result.upper())

def hexaToBin(hexa):     
    binary = bin(int(hexa, 16))
    binary = binary[2:] + ""   
    return binary
