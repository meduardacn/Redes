#https://www.youtube.com/watch?v=du_boiwX1yU
# zero | go back to the other side and come back again to the same side
# one  | make a transition to thother side and same transition from the manchester encoding
class MDIF():
    def encode(binary):
        result = ""
        if binary[0] == "0":
            result += "+"
            result += "-"
        elif binary[0] == "1":
            result += "-"
            result += "+"
        for i in range(1,len(binary)):
            if binary[i] == "0" and result[-1:] == "-":
                result += "+"
                result += "-"
            elif binary[i] == "0" and result[-1:] == "+":
                result += "-"
                result += "+"
            elif binary[i] == "1" and result[-1:] == "-":
                result += "-"
                result += "+"
            elif binary[i] == "1" and result[-1:] == "+":
                result += "+"
                result += "-"
        print(result)

    def decode(binary):
        result = ""
        if binary[0] == "0":
            result += "-"
        elif binary[0] == "1":
            result += "+"
        for i in range(1,len(binary)):
            if binary[i] == "0":
                result += result[i-1]
            elif result[i-1] == "-":
                result += "+"
            elif result[i-1] == "+":
                result += "-"
        print(result)