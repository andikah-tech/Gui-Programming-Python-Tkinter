from tkinter import *

master = Tk()

var = IntVar()

question = Label(master, text="what is your favorit languague!")

check1 = Checkbutton(master, text="java", variable=var)
check2 = Checkbutton(master, text="javascript", variable=var)
check3 = Checkbutton(master, text="php", variable=var)
check4 = Checkbutton(master, text="python", variable=var)

question.pack()
check1.pack(side="left")
check2.pack(side="left")
check3.pack(side="left")
check4.pack(side="left")

master.mainloop()