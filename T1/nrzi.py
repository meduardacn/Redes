class NRZI():
    def encode(binary):
        result = ''
        if binary[0] == '0':
            result += '-'
        elif binary[0] == '1':
            result += '+'
        for i in range(1,len(binary)):
            if binary[i] == '0':
                result += result[i-1]
            elif result[i-1] == '-':
                result += '+'
            elif result[i-1] == '+':
                result += '-'
        print(result)

    def decode(sinal):
        result = ''
        if sinal[0] == '+':
            result += '1'
        elif sinal[0] == '-':
            result += '0'

        for i in range(1,len(sinal)):
            if sinal[i] == sinal[i-1]:
                result += '0'
            elif sinal[i-1] == '-' and sinal[i] == '+':
                result += '1'
            elif sinal[i-1] == '+' and sinal[i] == '-':
                result += '1'
            
        result = hex(int(result, 2)) 
        return(result)