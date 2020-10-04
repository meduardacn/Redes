class EightB6T():
    def table():
        f = open("eightb6t.txt", "r")
        text = f.read()
        text = text.split("\n")
        table = dict()
        for elem in text:
            value = elem.split(" ")
            table[value[0]] = value[1]
        return(table)

    def encode(hexa):
        print(hexa)
        table = EightB6T.table()
        i = 0
        n = int(len(hexa)/2)
        result = ""
        resultPlus = 0
        resultMinus = 0
        for i in range(0,n):
            key = hexa[i*2:(i+1)*2]
            if resultMinus != resultPlus:
                value = table[key]
                newValue = ''
                for elem in newValue:
                    if elem == '+':
                        newValue += '-'
                    elif elem == '-':
                        newValue += '+'
                    elif elem == '0':
                        newValue += '0'
                result += newValue
                resultMinus += newValue.count('-')
                resultPlus += newValue.count('+')
                print(resultMinus,resultPlus)
            else:
                result += table[key]
                resultMinus += table[key].count('-')
                resultPlus += table[key].count('+')
                print(resultMinus,resultPlus)
        print(result)  

    def decode():
        return 0
