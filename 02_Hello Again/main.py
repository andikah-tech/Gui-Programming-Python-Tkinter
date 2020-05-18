import tkinter as tk

# template
class App(tk.Frame):
	
	# constructor __init__()
	def __init__(self,master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		# create quit button
		self.quit = tk.Button(self, text="QUIT", fg="red", command=master.destroy)
		self.quit.pack(side="left")
		# create click button
		self.hi = tk.Button(self)
		self.hi["text"] = "Click Here!"
		self.hi["command"] = self.click
		self.hi.pack(side="right")


	# method 
	def click(self):
		print("Hello, I'm GUI *_*")


root = tk.Tk()
root.title("GUI *_*")
# object
hello = App(master=root)
hello.mainloop()