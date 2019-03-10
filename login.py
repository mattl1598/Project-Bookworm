import hashlib
from tkinter import *
import json
import sql
import gui
import locations
import elevate


def gettheme():
	# get colours from json file

	with open(locations.theme(), "r") as readfile:
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


class Login:

	def __init__(self):
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, self.current_theme = gettheme()

		self.root = Tk()
		self.root.config(background=bg)
		debug = True

		relw = 400 / 1920
		relh = 180 / 1080

		size = str(int((self.root.winfo_screenwidth() * relw)))
		x = "x"
		size += x
		size += str(int(self.root.winfo_screenheight() * relh))

		self.root.geometry(size)
		self.root.title("Login - Project Bookworm")
		self.root.iconbitmap(locations.icons() + "\\colour.ico")

		self.root.user = Text(self.root, background=box_bg, foreground=box_txt, insertbackground=cursor,
										selectbackground=select)
		self.root.userL = Label(self.root, foreground=text, bg=bg, text="Username:")

		self.root.user.place(relx=19/40, rely=4/18, relheight=23/180, relwidth=180/400, anchor="w")
		self.root.userL.place(relx=19/40, rely=4/18, anchor="e")

		self.root.psw = Entry(self.root, background=box_bg, foreground=box_txt, insertbackground=cursor,
								selectbackground=select, show="*")
		self.root.pswL = Label(self.root, foreground=text, bg=bg, text="Password:")

		self.root.psw.place(relx=19 / 40, rely=80 / 180, relheight=23 / 180, relwidth=180 / 400, anchor="w")
		self.root.pswL.place(relx=19 / 40, rely=80 / 180, anchor="e")

		self.root.button = Button(self.root, command=lambda: self.log_me_in(debug), text="Log In", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)
		self.root.button.place(relx=1/2, rely=12/20)

		'''self.root.logo_img = PhotoImage(file="./icons/colour.gif")
		self.root.canvas = Canvas(self.root, width=63, height=63)
		self.root.canvas.create_image()
		self.root.canvas.place(relx=4/40, rely=30/180)
'''
		def focus_next(widget):
			widget.tk_focusNext().focus_set()
			return "break"

		def focus_prev(widget):
			widget.tk_focusPrev().focus_set()
			return "break"

		for i in (self.root.user, self.root.psw):
			i.bind('<Tab>', lambda e, t=i: focus_next(t))
			i.bind('<Shift-Tab>', lambda e, t=i: focus_prev(t))
			i.bind('<Return>', lambda e, t=i: self.log_me_in(debug))

		self.root.mainloop()

	def log_me_in(self, debug):
		if debug:
			print("yeet")
		flag = False
		user = self.root.user.get("0.0", 'end-1c')
		if debug:
			print("yeeet")
		psw = self.root.psw.get()
		if debug:
			print("yeeeet")
		logins = sql.get_logins()
		if debug:
			print("yeeeeet")
		ids = []
		users = []
		psws = []
		admin = []
		if debug:
			print("yeeeeeet")
		for i in range(len(logins)):
			ids.append(logins[i][0])
			users.append(logins[i][1])
			psws.append(logins[i][2])
			admin.append(logins[i][3])
			if debug:
				print("yeeeeeeet")
		if user in users:
			if debug:
				print("yeeeeeeeet")
			if hash_it(psw) == psws[users.index(user)]:
				print("Authentication Successful")
				setts = locations.settings()
				with open(setts, "r") as readfile:
					settings = json.load(readfile)
				settings["last_user_id"] = str(ids[users.index(user)])
				with open(setts, "w") as file:
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
	hash1 = hashlib.sha512(pwd.encode())
	hex1 = hash1.hexdigest()
	return hex1


def main():
	# elevate.elevate(show_console=True)
	Login()


if __name__ == "__main__":
	main()
