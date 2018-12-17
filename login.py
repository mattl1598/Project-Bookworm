import hashlib
from tkinter import *
import json
import sql
import gui

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

		self.root.psw = Entry(self.root, background=box_bg, foreground=box_txt, insertbackground=cursor,
								selectbackground=select, show="*")
		self.root.pswL = Label(self.root, foreground=text, bg=bg, text="Password:")

		self.root.psw.place(relx=19 / 40, rely=80 / 200, relheight=23 / 180, relwidth=180 / 400, anchor="w")
		self.root.pswL.place(relx=19 / 40, rely=80 / 200, anchor="e")

		self.root.button = Button(self.root, command=self.logmein)
		self.root.button.place(relx=1/2, rely=12/20)

		def focus_next(widget):
			widget.tk_focusNext().focus_set()
			return "break"

		def focus_prev(widget):
			widget.tk_focusPrev().focus_set()
			return "break"

		for t in (self.root.user, self.root.psw):
			t.bind('<Tab>', lambda e, t=t: focus_next(t))
			t.bind('<Shift-Tab>', lambda e, t=t: focus_prev(t))
			t.bind('<Return>', lambda e, t=t: self.logmein())

		self.root.mainloop()

	def logmein(self):
		flag = False
		user = self.root.user.get("0.0", 'end-1c')
		psw = self.root.psw.get()
		logins = sql.get_logins()

		ids = []
		users = []
		psws = []
		admin = []
		for i in range(len(logins)):
			ids.append(logins[i][0])
			users.append(logins[i][1])
			psws.append(logins[i][2])
			admin.append(logins[i][3])

		if user in users:
			if hash_it(psw) == psws[users.index(user)]:
				print("Authentication Successful")
				with open("D:/Project-Bookworm/settings.json", "r") as readfile:
					settings = json.load(readfile)
				settings["last_user_id"] = str(ids[users.index(user)])
				with open("D:/Project-Bookworm/settings.json", "w") as file:
					json.dump(settings, file, indent=4)

				flag = True
			else:
				print("Authentication Failed")
		else:
			print("Authentication Failed")

		if flag is True:
			self.root.destroy()
			gui.homescreen()

def hash_it(pwd):
	hash = hashlib.sha512(pwd.encode())
	hex = hash.hexdigest()
	return hex

def main():
	login1 = login()


if __name__ == "__main__":
	main()



