from tkinter import *

window = Tk()
window.title("CALCULATER")
window.minsize(height=300, width=200)
window.config(padx=20, pady=20, bg="pink")
# entry
entry = Entry()
entry.config(width=40)
entry.grid(row=0, column=0, columnspan=4)


def button_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + value)


def evaluate():
    expression = str(entry.get())
    try:
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, result)
    except EXCEPTION:
        entry.delete(0, END)
        entry.insert(0, "Error")


def clear():
    entry.delete(0, END)


Buttons = ["7", "8", "9", "/",
           "4", "5", "6", "*",
           "1", "2", "3", "-",
           "C", "0", "=", "+"]
Row = 1
Col = 0
for b in Buttons:
    if b == "=":
        botn = Button(text=b, pady=20, padx=20, command=evaluate)
        botn.grid(row=Row, column=Col)
    elif b == "C":
        botn = Button(text=b, pady=20, padx=20, command=clear)
        botn.grid(row=Row, column=Col)
    else:
        botn = Button(text=b, pady=20, padx=20, command=lambda b1=b: button_click(b1))
        botn.grid(row=Row, column=Col)
    Col = Col + 1
    if Col > 3:
        Row = Row + 1
        Col = 0
window.mainloop()
