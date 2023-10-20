from tkinter import *

window=Tk()
window.title("MILES TO KM")
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)

#label1
label=Label(text="Miles")
label.grid(row=0,column=2)

#label2
label2=Label(text="is equal to")
label2.grid(row=1,column=0)

#label3
label3=Label(text="Km")
label3.grid(row=1,column=2)

#km label
label_km=Label(text=0)
label_km.grid(row=1,column=1)

#entry
entry=Entry()
entry.grid(row=0,column=1)

#mile to km converter function
def m_to_k():
    miles=float(entry.get())
    km=miles*1.609
    label_km.config(text=km)

#button
button=Button(text="CALCULATE",command=m_to_k)
button.grid(row=2,column=1)


window.mainloop()