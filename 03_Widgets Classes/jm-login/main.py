from tkinter import *

# template
class Jm_login(Frame):

	# const __init__()
	def __init__(self,master=None):
		super().__init__(master)
		self.master = master
		self.grid()
		self.form_login()

	# method
	def form_login(self):

		# username
		self.lbluser = Label(self, text="username")
		self.lbluser.grid(row=0,column=0)
		self.entuser = Entry(self)
		self.entuser.grid(row=0,column=1)

		# password 
		self.lblpass = Label(self, text="password")
		self.lblpass.grid(row=1,column=0)
		self.entpass = Entry(self, show="*")
		self.entpass.grid(row=1,column=1)

		# checked
		self.login = Button(self)
		self.login["text"] = "login"
		self.login["command"] = self.clicked
		self.login.grid(columnspan=2)

	def clicked(self):
		
		username = self.entuser.get()
		password = self.entpass.get()

		if username.lower() == "jm-kodigu" and password.lower() == "jmfromtl":
			print("LOGIN SUCCESS!")
		elif len(username) == 0 and len(password) == 0 :
			print(None)
		else:
			self.info = Label(self)
			self.info["text"] = "Username or Password Incorrect"
			self.info["fg"] = "red"
			self.info.grid(columnspan=2)


root = Tk()
root.title("Login")
# object
app = Jm_login(master=root)
root.mainloop()
root.quit()
