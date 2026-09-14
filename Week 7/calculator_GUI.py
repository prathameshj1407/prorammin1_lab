import tkinter as tk

window: tk = tk.Tk()
window.title('Simple Calculator GUI')
window.geometry('500x500')

tk.Label(window, text="First number: ").pack()
num1 = tk.Entry(window)
num1.pack()

tk.Label(window, text="Second number: ").pack()
num2 = tk.Entry(window)
num2.pack()

def add():
    number1 = num1.get()
    number2 = num2.get()
    calculation = float(number1) + float(number2)
    result.config(text = "output: " + str(calculation))

def sub():
    number1 = num1.get()
    number2 = num2.get()
    calculation = float(number1) - float(number2)
    result.config(text = "output: " + str(calculation))

def mul():
    number1 = num1.get()
    number2 = num2.get()
    calculation = float(number1) * float(number2)
    result.config(text = "output: " + str(calculation))

def div():
    number1 = num1.get()
    number2 = num2.get()
    calculation = float(number1) / float(number2)
    result.config(text = "output: " + str(calculation))

def avg():
    number1 = num1.get()
    number2 = num2.get()
    calculation = float(number1) + float(number2) / 2
    result.config(text = "output: " + str(calculation))

tk.Button(window, text="Addition", command=add).pack()
tk.Button(window, text="Subraction", command=sub).pack()
tk.Button(window, text="Multiplication", command=mul).pack()
tk.Button(window, text="Division", command=div).pack()
tk.Button(window, text="Average", command=avg).pack()
result = tk.Label(window, text="output here: ")
result.pack()

window.mainloop()