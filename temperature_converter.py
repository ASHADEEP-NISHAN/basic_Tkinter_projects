from tkinter import *

# CONFIGURE SCREEN
window = Tk()
window.minsize(500, 500)
window.config(padx=20, pady=20)
window.title("TEMPERATURE CONVERTER")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def convert_temperature():
    try:
        temperature = float(entry1.get())
        if temperature_unit.get() == "Celsius":
            result = celsius_to_fahrenheit(temperature)
            result_label.config(text=f"{temperature} °C = {result} °F")
        else:
            result = fahrenheit_to_celsius(temperature)
            result_label.config(text=f"{temperature} °F = {result} °C")
    except ValueError:
        result_label.config(text="Invalid input")


# TEMPERATURE CONVERTER LABEL
label1 = Label(text="Temperature Converter")
label1.config(pady=20, padx=20, font=("Arial", 30, "bold"))
label1.pack()

# celcius label
label2 = Label(text="Enter Temperature")
label2.config(pady=20, padx=20, font=("Arial", 20, "bold"))
label2.pack()

# entry
entry1 = Entry(width=50)
entry1.pack()


temperature_unit = StringVar()
temperature_unit.set("Celsius")
# select unit label
label3 = Label(text="Select Unit:")
label3.config(padx=20, pady=20, font=("Arial", 20, "bold"))
label3.pack()

# radio button celsius
celsius = Radiobutton(text="Celsius", variable=temperature_unit,
                      value="Celsius",font=("Arial", 20, "bold"))
celsius.pack()
# radio button fahrenheit
fahrenheit=Radiobutton(text="fahrenheit",variable=temperature_unit,
                       value="Fahrenheit",font=("Arial", 20, "bold"))
fahrenheit.pack()

#button
convert=Button(text="CONVERT",command=convert_temperature)
convert.pack()
#result label
result_label=Label()
result_label.config(pady=20,padx=20,font=("Arial", 20, "bold"))
result_label.pack()

window.mainloop()
