from tkinter import *

master = Tk()

def ok():
	print(e.get())

var= StringVar()

l = Label(master, text="input any data!")
l.grid(row=0,column=0)

e = Entry(master, textvariable=var)
e.grid(row=0,column=1)

var.set("default value!")

c = Button(master, text="OK", command=ok)
c.grid(columnspan=2)

mainloop()