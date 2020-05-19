'''
from tkinter import *

master = Tk()

x = Canvas(master, width=200, height=100)
x.pack()

x.create_line(0,0,200,100, fill="green", dash=(3,4))
x.create_line(0,100,200,0, fill="red", dash=(4,4))

x.create_rectangle(50,25,150,75, fill="blue")

master.mainloop()
'''

# my draw with Canvas class
from tkinter import *

# template
class Draw(Frame):
	
	# constructor __init__()
	def __init__(self,master=None):
		# call superclass & cons __init__()
		super().__init__(master)
		self.master = master
		self.grid()
		# call create_draw method
		self.button = Button(self, text="view!", fg="blue", command=self.create_draw)
		self.button.grid(row=0, column=0)
		# quit button
		self.quit = Button(self, text="QUIT", fg="white", bg="red", command=self.master.destroy).grid(row=0, column=1)

	# method
	def create_draw(self):
		self.draw1 = Canvas(self, width=200, height=100)
		self.draw1.grid(columnspan=2)

		self.draw1.create_line(0,0,200,100, fill="green", dash=(5,1))
		self.draw1.create_line(0,100,200,0, fill="red", dash=(4,4))
		self.draw1.create_rectangle(50,25,150,75, fill="pink")


root = Tk()
# object
file = Draw(master=root)
file.mainloop()