class HDB3():
    def encode(binary):
        infoBit = '-'
        countZero = 0
        verifyBit = '-'
        i = 0
        result = ['|' for _ in range(len(binary))]
        for i in range(0,len(binary)):
            if binary[i] == '1':
                countZero = 0
                if infoBit == '-':
                    result[i] = '+'
                    infoBit = '+'
                else:
                    result[i] = '-'
                    infoBit = '-'
            elif binary[i] == '0' and countZero == 3:
                if verifyBit == '-':
                    result[i] = '+'
                    verifyBit = '+'
                    if infoBit != verifyBit:
                        result[i-3] = '+' 
                    infoBit   = '+'
                else:
                    result[i] = '-'
                    verifyBit = '-'
                    if infoBit != verifyBit:
                        result[i-3] = '-'
                    infoBit   = '-'
                countZero = 0
            elif binary[i] == '0' and countZero < 3:
                result[i] = '0'     
                countZero += 1
        resultStr = ''
        for elem in result:
            resultStr += elem
        print(resultStr)

    def decode(sinal):
        infoBit = '-'
        countZero = 0
        verifyBit = '-'
        i = 0
        result = ['|' for _ in range(len(sinal))]
        for i in range(0,len(sinal)):   
            if sinal[i] != '0':
                result[i] = '1'
            else:
                result[i] = '0'
        change = 0
        for i in range(0,len(sinal)):
            if change == 1:
                change = 0
                continue
            if result[i] == '1':
                countZero = 0
            if result[i] == '0':
                countZero += 1
                print(sinal[:i+1])
                if countZero == 3 and (sinal[i+1] == sinal[i-3]):
                    print("eae")
                    change = 1
                    result[i+1] = '0'
                    countZero = 0
                elif countZero == 2:
                    print("entre")
                    change = 1
                    if sinal[i-3] == sinal[i+1]:
                        result[i+1] = '0'
                        result[i-2] = '0'
                    countZero = 0
                
        resultStr = ''
        for elem in result:
            resultStr += elem
        print(resultStr)