import math_utils

x = int(input("Enter a number for x"))
y = int(input("Enter a number for y"))
operator = input("Enter a the operator")

Dict = {"+" : math_utils.add(x,y),
        "-" : math_utils.subtract(x,y),
        "*" : math_utils.multiply(x,y),
        "/" : math_utils.divide(x,y),
        "pow" : math_utils.power(x,y),
        "%" : math_utils.mod(x,y),
        }
def myFunction():
        if operator == "+":
                print(Dict["+"])
        elif operator == "-":
                print(Dict["-"])
        elif operator == "*":
                print(Dict["*"])
        elif operator == "/":
                print(Dict["/"])
        elif operator == "pow":
                print(Dict["pow"])
        elif operator == "%":
                print(Dict["%"])
        else:
                print("Invalid input")

def main():
        myFunction()

if __name__ == "__main__":
        main()
