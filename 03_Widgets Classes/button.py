from tkinter import *

root = Tk()
root.title("Button")

def callback():
	print("Click!")

x = Button(root, text="OK", command=callback)
x.pack()

root.mainloop()