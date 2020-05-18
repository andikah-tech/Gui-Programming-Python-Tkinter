from tkinter import *

# template
class App(Frame):

	# constructor __init__
	def __init__(self,master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		# call widgets method
		self.widgets()

	# method
	def widgets(self):
		# set label
		self.label = Label(self, text="Hello I'm GUI *_*").grid(columnspan=2)
		# click button
		self.hi = Button(self)
		self.hi["text"] = "Click Here!"
		self.hi["command"] = self.ok
		self.hi.grid(row=1, column=0)

		# quit button
		self.quit = Button(self)
		self.quit["text"] = "QUIT"
		self.quit["command"] = self.master.destroy
		self.quit["fg"] = "red"
		self.quit.grid(row=1, column=1)

	def ok(self):
		self.click = Label(self, text="Button Onclick!", fg="blue").grid(columnspan=2)


root = Tk()
root.title("Hello Again")
# object
myapp = App(master=root)
myapp.mainloop()