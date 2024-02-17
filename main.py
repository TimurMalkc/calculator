import tkinter as tk

import ctypes


def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def toPostFix(equation):
    postfixEquation = ""
    operatorStack = ["("]
    operators = ["+","-","/","*","(",")"]
    tempStr = ""
    equation += ")"

    for i in equation:
        if isNumber(i) or i == ".":
            tempStr += i
        elif i in operators:
            if (tempStr != ""):
                postfixEquation += tempStr + " "
                tempStr = ""
            if i == "(":
                operatorStack.append(i)
            elif i == "*" or i == "/":
                if (len(operatorStack) != 0) and (operatorStack[-1] == "/" or operatorStack[-1] == "*"):
                    postfixEquation += operatorStack[-1] + " "
                    operatorStack.pop()
                    operatorStack.append(i)
                else:
                    operatorStack.append(i)
            elif i == "+" or i == "-":
                if (len(operatorStack) != 0) and (operatorStack[-1] == "/" or operatorStack[-1] == "*" or operatorStack[-1] == "+" or operatorStack[-1] == "-" ):
                    postfixEquation += operatorStack[-1] + " "
                    operatorStack.pop()
                    operatorStack.append(i)
                else:
                    operatorStack.append(i)
            else:
                while(operatorStack[-1] != "("):
                    postfixEquation += operatorStack[-1] + " "
                    operatorStack.pop()
                operatorStack.pop()
        else:
            return "Invalid input"

    if (tempStr != ""):
        postfixEquation += tempStr + " "

    return postfixEquation

def evaluatePostfix(equation):
    stackNums = []
    myRes = 0
    equation = equation.split()

    for i in equation:
        if isNumber(i):
            stackNums.append(float(i))
        else:
            if(i == "+"):
                myRes = stackNums[-2] + stackNums[-1]
            elif(i == "-"):
                myRes = stackNums[-2] - stackNums[-1]
            elif (i == "*"):
                myRes = stackNums[-2] * stackNums[-1]
            else:
                if(stackNums[-1] == 0):
                    return "Zero division error"
                else:
                    myRes = stackNums[-2] / stackNums[-1]
            stackNums.pop()
            stackNums.pop()
            stackNums.append(myRes)
            myRes = 0

    return float(stackNums[0])


#mystr = input()
#mystr = toPostFix(mystr)
#print(evaluatePostfix(mystr))

window = tk.Tk()
window.title("Calculator")

window.geometry("600x800")

myText = tk.Text(window, height = 5, width = 52)

myLabel = tk.Label(window, text="Calculator")
myLabel.config(font =("Courier", 14))



tk.Button(window, text="Calculate").grid(column=1, row=0)

ctypes.windll.shcore.SetProcessDpiAwareness(True)

window.mainloop()