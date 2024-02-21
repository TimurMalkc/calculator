import tkinter as tk
import ctypes

equation = ""
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def toPostFix():
    global equation
    postfixEquation = ""
    operatorStack = ["("]
    operators = ["+","-","/","*","(",")"]
    tempStr = ""

    if (equation == ""):
        return

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

def evaluatePostfix():
    global equation
    stackNums = []
    myRes = 0

    if (equation == None):
        return

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

    if(float(stackNums[0]) == int(stackNums[0])):
        return int(stackNums[0])
    else:
        return float(stackNums[0])

def submit():
    global equation
    equation = entry.get()
    equation = toPostFix()
    delete()
    entry.insert(0, evaluatePostfix())

def delete():
    entry.delete(0, tk.END)
def backspace():
    entry.delete(len(entry.get())-1 ,tk.END)

def insertText(char):
    entry.insert(len(entry.get()), char)

window = tk.Tk()
window.title("Calculator")
window.geometry("600x800")
window.config(background="#34ebb4")

frameEntry = tk.Frame(window, pady=5, background="#34ebb4")
frameEntry.pack()
frameButtons = tk.Frame(window,pady=5, background="#34ebb4")
frameButtons.pack()

entry = tk.Entry(frameEntry, font=("Ariel",30))
entry.grid(row = 0, column = 0, sticky = tk.W, pady = 2)


button1 = tk.Button(frameButtons, text="1", command = lambda: insertText("1"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
button1.grid(row = 0, column = 0, sticky = tk.W, pady = 2)
button2 = tk.Button(frameButtons, text="2", command = lambda: insertText("2"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
button2.grid(row = 0, column = 1, sticky = tk.W, pady = 2)
button3 = tk.Button(frameButtons, text="3", command = lambda: insertText("3"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
button3.grid(row = 0, column = 2, sticky = tk.W, pady = 2)
button4 = tk.Button(frameButtons, text="4", command = lambda: insertText("4"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
button4.grid(row = 1, column = 0, sticky = tk.W, pady = 2)
button5 = tk.Button(frameButtons, text="5", command = lambda: insertText("5"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
button5.grid(row = 1, column = 1, sticky = tk.W, pady = 2)
button6 = tk.Button(frameButtons, text="6", command = lambda: insertText("6"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
button6.grid(row = 1, column = 2, sticky = tk.W, pady = 2)
button7 = tk.Button(frameButtons, text="7", command = lambda: insertText("7"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
button7.grid(row = 2, column = 0, sticky = tk.W, pady = 2)
button8 = tk.Button(frameButtons, text="8", command = lambda: insertText("8"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
button8.grid(row = 2, column = 1, sticky = tk.W, pady = 2)
button9 = tk.Button(frameButtons, text="9", command = lambda: insertText("9"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
button9.grid(row = 2, column = 2, sticky = tk.W, pady = 2)
button0 = tk.Button(frameButtons, text="0", command = lambda: insertText("0"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
button0.grid(row = 3, column = 0, sticky = tk.W, pady = 2)
buttonP1 = tk.Button(frameButtons, text="(", command = lambda: insertText("("), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
buttonP1.grid(row = 3, column = 1, sticky = tk.W, pady = 2)
buttonP2 = tk.Button(frameButtons, text=")", command = lambda: insertText(")"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
buttonP2.grid(row = 3, column = 2, sticky = tk.W, pady = 2)
buttonDot = tk.Button(frameButtons, text=".", command = lambda: insertText("."), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
buttonDot.grid(row = 4, column = 0, sticky = tk.W, pady = 2)
buttonBs = tk.Button(frameButtons, text="<-", command=backspace, font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
buttonBs.grid(row = 4, column = 1, sticky = tk.W, pady = 2)
buttonCl = tk.Button(frameButtons, text="Cl", command=delete, font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
buttonCl.grid(row = 4, column = 2, sticky = tk.W, pady = 2)
buttonPlus = tk.Button(frameButtons, text="+", command = lambda: insertText("+"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
buttonPlus.grid(row = 0, column = 3, sticky = tk.W, pady = 2, padx=(40,0))
buttonMin = tk.Button(frameButtons, text="-", command = lambda: insertText("-"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
buttonMin.grid(row = 1, column = 3, sticky = tk.W, pady = 2, padx=(40,0))
buttonMul = tk.Button(frameButtons, text="*", command = lambda: insertText("*"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
buttonMul.grid(row = 2, column = 3, sticky = tk.W, pady = 2, padx=(40,0))
buttonDiv = tk.Button(frameButtons, text="/", command = lambda: insertText("/"), font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
buttonDiv.grid(row = 3, column = 3, sticky = tk.W, pady = 2, padx=(40,0))
buttonEq = tk.Button(frameButtons, text="=", command = submit, font=("Comic Sans", 30), fg="blue", bg="purple", activeforeground="blue", activebackground="purple", width=5)
buttonEq.grid(row = 4, column = 3, sticky = tk.W, pady = 2, padx=(40,0))


ctypes.windll.shcore.SetProcessDpiAwareness(True)

window.mainloop()