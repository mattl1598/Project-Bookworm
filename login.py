import hashlib
from tkinter import *
import json
import sql

def gettheme():
	# get colours from json file
	with open("D:/Project-Bookworm/theme.json", "r") as readfile:
		theme1 = json.load(readfile)

	theme = theme1["theme"]

	bg = theme1[theme]["windows"]["background"]
	text = theme1[theme]["windows"]["text"]
	button_bg = theme1[theme]["button"]["background"]
	butt_txt = theme1[theme]["button"]["text"]
	box_bg = theme1[theme]["textbox"]["background"]
	box_txt = theme1[theme]["textbox"]["foreground"]
	cursor = theme1[theme]["textbox"]["insertbackground"]
	select = theme1[theme]["textbox"]["selectbackground"]
	clickedbg = theme1[theme]["button"]["clickedbg"]

	return bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, theme

class login():

	def __init__(self):
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, self.current_theme = gettheme()

		self.root = Tk()
		self.root.config(background=bg)

		relw = 400 / 1920
		relh = 180 / 1080

		size = str(int((self.root.winfo_screenwidth() * (relw))))
		x = "x"
		size += x
		size += str(int(self.root.winfo_screenheight() * (relh)))

		self.root.geometry(size)

		self.root.user = Text(self.root, background=box_bg, foreground=box_txt, insertbackground=cursor,
										selectbackground=select)
		self.root.userL = Label(self.root, foreground=text, bg=bg, text="Username:")

		self.root.user.place(relx=19/40, rely=4/20, relheight=23/180, relwidth=180/400, anchor="w")
		self.root.userL.place(relx=19/40, rely=4/20, anchor="e")

		self.root.psw = Text(self.root, background=box_bg, foreground=box_txt, insertbackground=cursor,
		                      selectbackground=select)
		self.root.pswL = Label(self.root, foreground=text, bg=bg, text="Password:")

		self.root.psw.place(relx=19 / 40, rely=80 / 200, relheight=23 / 180, relwidth=180 / 400, anchor="w")
		self.root.pswL.place(relx=19 / 40, rely=80 / 200, anchor="e")

		self.root.button = Button(self.root, command=self.logmein)
		self.root.button.place(relx=1/2, rely=12/20)

		self.root.mainloop()

	def logmein(self):
		user = self.root.user.get("0.0", 'end-1c')
		psw = self.root.psw.get("0.0", 'end-1c')
		print(user, " ", psw)

def hash_it(pwd):
	hash = hashlib.sha512(pwd.encode())
	hex = hash.hexdigest()
	print(hex)


login1 = login()

hash_it("test")

print(sql.get_logins())