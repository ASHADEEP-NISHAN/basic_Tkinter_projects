from tkinter import *

window = Tk()
window.title("CALCULATER")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)

# label 1
enter1 = Label(text="ENTER FIRST NUMBER")
enter1.grid(row=0, column=0)
enter1.config(padx=20, pady=20)

# Label 2
enter2 = Label(text="ENTER SECOND NUMBER")
enter2.grid(row=1, column=0)
enter1.config(pady=20, padx=20)

# Label 3
answer = Label(text="ANSWER")
answer.grid(row=2, column=0)
answer.config(padx=20, pady=20)

# entry1
entry1 = Entry()
entry1.grid(row=0, column=1)

# entry2
entry2 = Entry()
entry2.grid(row=1, column=1)

# answer label
output = Label(text=0)
output.grid(row=2, column=1)


# global variables


# add function
def addition():
    a = float(entry1.get())
    b = float(entry2.get())
    c = a + b
    answer.config(text="Addition is")
    output.config(text=c)


# addition button
add = Button(text="ADD",width=6, command=addition)
add.grid(row=0, column=2)
add.config(padx=20, pady=20)


# subtraction function
def subtraction():
    a = float(entry1.get())
    b = float(entry2.get())
    d = a - b
    answer.config(text="Subtraction is")
    output.config(text=d)


# subtraction button
sub = Button(text="SUBTRACT",width=6, command=subtraction)
sub.grid(row=1, column=2)
sub.config(pady=20, padx=20)


# multiplication function
def multiplication():
    a = float(entry1.get())
    b = float(entry2.get())
    e = a * b
    answer.config(text="Multiplication is")
    output.config(text=e)


# multiplication button
mul = Button(text="MULTIPLY",width=6, command=multiplication)
mul.grid(row=2, column=2)
mul.config(pady=20, padx=20)


# division function
def division():
    a = float(entry1.get())
    b = float(entry2.get())
    f = a / b
    answer.config(text="Division is")
    output.config(text=f)


# division button
div = Button(text="DIVISION",width=6, command=division)
div.grid(row=3, column=1)
div.config(padx=20, pady=20)


# modules function
def modules():
    a = float(entry1.get())
    b = float(entry2.get())
    g = a % b
    answer.config(text="Modules is")
    output.config(text=g)


# modulus button
mod = Button(text="MODULUS",width=6, command=modules)
mod.grid(row=3, column=2)
mod.config(pady=20, padx=20)

window.mainloop()
