from tkinter import *

# template
class App2(Frame):

	# constructor __init__()
	def __init__(self,master=None):
		# call superclass and __init__
		super().__init__(master)
		self.master = master
		self.pack()
		# call widgets method
		self.create_widgets()

	# method
	def create_widgets(self):
		self.hello = Button(self)
		self.hello["text"] = "Click Here!"
		self.hello["command"] = self.event_click
		self.hello.pack()

		self.quit = Button(self, text="QUIT", fg="white", bg="red", command=self.master.destroy).pack()

	def event_click(self):
		print("Hello, World!")


root = Tk()
# object
myapp = App2(master=root)
myapp.mainloop()