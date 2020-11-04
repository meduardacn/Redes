#https://www.youtube.com/watch?v=du_boiwX1yU
# zero | go back to the other side and come back again to the same side
# one  | make a transition to thother side and same transition from the manchester encoding
class MDIF():
    def encode(binary):
        result = ''
        if binary[0] == '0':
            result += '+'
            result += '-'
        elif binary[0] == '1':
            result += '-'
            result += '+'
        for i in range(1,len(binary)):
            if binary[i] == '0' and result[-1:] == '-':
                result += '+'
                result += '-'
            elif binary[i] == '0' and result[-1:] == '+':
                result += '-'
                result += '+'
            elif binary[i] == '1' and result[-1:] == '-':
                result += '-'
                result += '+'
            elif binary[i] == '1' and result[-1:] == '+':
                result += '+'
                result += '-'
        print(result)

    def decode(sinal):
        result = ''
        if sinal[0] == '+' and sinal[1] == '-':
            result += '0'
        elif sinal[0] == '-' and sinal[1] == '+':
            result += '1'
        i = 2
        while i < len(sinal):
            if sinal[i-1] == '-' and sinal[i] == '-':
                result += '1'
            elif sinal[i-1] == '+' and sinal[i] == '+':
                result += '1'
            else:
                result += '0'
            i += 2
        result = hex(int(result, 2))[2:]
        print(result.upper())
