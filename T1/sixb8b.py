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

    def decode():
        return 0