import tkinter as tk
import ctypes

equation = ""
isInvalid = False
validOperators = ["+","-","/","*","(",")"]

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def toPostFix(equation):
    global validOperators
    postfixEquation = ""
    operatorStack = ["("]
    tempStr = ""

    if (equation == ""):
        return

    equation += ")"
    for i in equation:
        if isNumber(i) or i == ".":
            tempStr += i
        elif i in validOperators:
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
                    if equation.index(i) == 0:
                        return
            elif i == "+" or i == "-":
                if (len(operatorStack) != 0) and (operatorStack[-1] == "/" or operatorStack[-1] == "*" or operatorStack[-1] == "+" or operatorStack[-1] == "-" ):
                    postfixEquation += operatorStack[-1] + " "
                    operatorStack.pop()
                    operatorStack.append(i)
                else:
                    operatorStack.append(i)
                    if equation.index(i) == 0:
                        tempStr += "0 "
            else:
                while(operatorStack[-1] != "("):
                    postfixEquation += operatorStack[-1] + " "
                    operatorStack.pop()
                operatorStack.pop()
        else:
            return

    if (tempStr != ""):
        postfixEquation += tempStr + " "

    return postfixEquation

def evaluatePostfix(equation):
    try:
        stackNums = []
        myRes = 0

        if (equation == None):
            return

        equation = equation.split()
        for i in equation:
            if isNumber(i):
                stackNums.append(float(i))
            else:
                if (i == "+"):
                    myRes = stackNums[-2] + stackNums[-1]
                elif (i == "-"):
                    myRes = stackNums[-2] - stackNums[-1]
                elif (i == "*"):
                    myRes = stackNums[-2] * stackNums[-1]
                else:
                    myRes = stackNums[-2] / stackNums[-1]
                stackNums.pop()
                stackNums.pop()
                stackNums.append(myRes)

        if (float(stackNums[0]) == int(stackNums[0])):
            return int(stackNums[0])
        else:
            return float(stackNums[0])
    except Exception:
        return

def submit(equation):
    global isInvalid
    equation = entry.get()
    equation = toPostFix(equation)
    delete()
    if(evaluatePostfix(equation) != None):
        entry.insert(0, str(evaluatePostfix(equation)))
    else:
        isInvalid = True
        entry.insert(0, "Invalid")
        return

def delete():
    entry.delete(0, tk.END)

def backspace():
    entry.delete(len(entry.get())-1 ,tk.END)

def insertText(char):
    global isInvalid
    if isInvalid:
        isInvalid = False
        delete()
    entry.insert(len(entry.get()), char)

def newButton(text, command, fg, bg, row, column, padx):
    button = tk.Button(frameButtons, text=text, command=command, font=("Comic Sans", 30), fg=fg, bg=bg, activeforeground=fg, activebackground=bg, width=5 )
    button.grid(row=row, column=column, sticky=tk.W, pady=2, padx=(padx,0))
    return button

window = tk.Tk()
window.title("Calculator")
window.geometry("600x600")
window.config(background="#176B87")

frameEntry = tk.Frame(window, pady=30, background="#176B87")
frameEntry.pack()
frameButtons = tk.Frame(window, pady=5, background="#176B87")
frameButtons.pack()

entry = tk.Entry(frameEntry, font=("Ariel",35))
entry.grid(row = 0, column = 0, sticky = tk.W, pady = 2)
entry.focus()

for i in range(10):
    newButton(str((i+1)%10), lambda num = (i+1)%10: insertText(str(num)), "#EEF5FF", "#B4D4FF", i//3, i%3, 0)

for i in range(4):
    newButton(validOperators[i], lambda char=validOperators[i] : insertText(char), "#EEF5FF", "#86B6F6", i, 3, 40)

newButton("(", lambda: insertText("("), "#EEF5FF", "#B4D4FF", 3, 1, 0)
newButton(")", lambda: insertText(")"), "#EEF5FF", "#B4D4FF",3, 2, 0)
newButton(".", lambda: insertText("."), "#EEF5FF", "#B4D4FF",4, 0, 0)
newButton("<-", backspace, "#EEF5FF", "#B4D4FF", 4, 1, 0)
newButton("Cl", delete, "#EEF5FF", "#B4D4FF", 4, 2, 0)
newButton("=", lambda: submit(equation), "#EEF5FF", "#86B6F6", 4, 3, 40)

window.bind("<Return>", lambda x: submit(equation))

ctypes.windll.shcore.SetProcessDpiAwareness(True)

window.mainloop()