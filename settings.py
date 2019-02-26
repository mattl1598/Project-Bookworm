import tkinter
import homepage
import json
from tkinter import filedialog
from tkinter import messagebox
from IPy import IP
import sqlite3
import sql
import gui
import re
import hashlib
import locations

def gettheme():
	# get colours from json file
	setts = locations.settings()
	with open(setts, "r") as read2:
		settings = json.load(read2)

	rootpath = settings["root_location"]

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


class Options:

	def __init__(self):

		# import colours
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, self.current_theme = gettheme()

		setts = locations.settings()
		with open(setts, "r") as read2:
			setting = json.load(read2)

		rootpath = setting["root_location"]

		with open(rootpath + "theme.json", "r") as readfile:
			theme = json.load(readfile)

		self.current_db = setting["database_location"]
		self.current_root = setting["root_location"]
		self.db = self.current_db
		self.root = self.current_root

		self.setts = tkinter.Tk()

		relw = 55 / 192
		relh = 20 / 54

		size = str(int((self.setts.winfo_screenwidth() * (relw))))
		x = "x"
		size += x
		size += str(int(self.setts.winfo_screenheight() * (relh)))

		self.setts.geometry(size)
		self.setts.iconbitmap(locations.icons() + "\\settings.ico")
		self.setts.title("Settings")
		self.setts.configure(background=bg)

		themes = [
			"dark",
			"light",
			"custom"
		]

		self.theme = tkinter.StringVar(self.setts)
		self.theme.set(self.current_theme)

		# option menu setup and config
		self.themeDrop = tkinter.OptionMenu(self.setts, self.theme, *themes)
		self.themeDrop.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
									activeforeground=butt_txt, highlightthickness=0, highlightcolor=bg, highlightbackground=bg)
		self.themeDrop["menu"].config(bg=button_bg, foreground=butt_txt, bd="0", activebackground="SystemHighlight",
										activeforeground=butt_txt)
		self.setts.theme = tkinter.Label(self.setts, foreground=text, bg=bg, text="Theme:")

		self.setts.db_label = tkinter.Label(self.setts, foreground=text, bg=bg, text="Database:")
		self.db_location = tkinter.Text(self.setts, background=box_bg, foreground=box_txt, insertbackground=cursor,
										selectbackground=select)
		self.db_location.insert(tkinter.INSERT, self.db)
		self.db_button = tkinter.Button(text="Browse", command=lambda: self.db_browse(1), background=button_bg, foreground=butt_txt,
										activebackground=clickedbg, activeforeground=butt_txt)

		self.setts.root_label = tkinter.Label(self.setts, foreground=text, bg=bg, text="Root Folder:")
		self.setts.root_location = tkinter.Text(self.setts, background=box_bg, foreground=box_txt,
												insertbackground=cursor, selectbackground=select)
		self.setts.root_location.insert(tkinter.INSERT, self.root)
		self.setts.root_button = tkinter.Button(text="Browse", command=lambda: self.db_browse(0), background=button_bg,
												foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.setts.add_user = tkinter.Button(text="Add New User", command=self.new_user, background=button_bg,
												foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)



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

		setts = locations.settings()

		with open(setts, "r") as readfile:
			setts = json.load(readfile)

		isAdmin = tkinter.BooleanVar()
		isAdmin.set(admin[ids.index(int(setts["last_user_id"]))])

		if isAdmin.get() is True:
			self.setts.add_user.place(relx=0.5, rely=0.5, anchor="n")

		self.themeDrop.place(relx=0.5, rely=0.2, anchor="w")
		self.setts.theme.place(relx=0.5, rely=0.2, anchor="e")
		self.setts.db_label.place(relx=0.8-250/400, rely=0.3, anchor="e")
		self.db_location.place(relx=0.8, rely=0.3, relheight=19/300, relwidth=250/400, anchor="e")
		self.db_button.place(relx=0.8, rely=0.3, anchor="w")
		self.setts.root_label.place(relx=0.8 - 250 / 400, rely=0.4, anchor="e")
		self.setts.root_location.place(relx=0.8, rely=0.4, relheight=19 / 300, relwidth=250 / 400, anchor="e")
		self.setts.root_button.place(relx=0.8, rely=0.4, anchor="w")
		self.quit = tkinter.Button(text="Close", command=self.close)
		self.quit.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)
		self.quit.place(relx=0.5, rely=0.9)


		self.setts.mainloop()

	def apply(self, current_theme, current_db, db, root, current_root):
		db2 = self.db_location.get("1.0", "end")
		theme = self.theme.get()
		"""
		if db2 == current_db:
			print("yes")

		try:
			print(IP(db2))
			print("succeeded1")
		except ValueError:
			print("fail")
			try:
				print(db2)
				conn = sqlite3.connect(db2)
				c = conn.cursor()
				c.execute("SELECT * FROM schools")
				print(c.fetchall())
				conn.close()
				print("succeeded2")
				self.flag = True
			except sqlite3.OperationalError:
				print("double fail")
				self.flag = "dbFail"
		"""
		self.flag = True
		if self.flag != "dbFail":
			if theme != current_theme:
				themepath = locations.theme()

				with open(themepath, "r") as file:
					# doesnt work as one line. has to be two seperate "with opens" to modify a json.
					theme1 = json.load(file)

				theme1["theme"] = theme

				with open(themepath, "w") as file:
					json.dump(theme1, file, indent=4)

			if db != current_db or db is not None:
				setts2 = locations.settings()
				with open(setts2, "r") as file:
					# doesnt work as one line. has to be two seperate "with opens" to modify a json.
					setts = json.load(file)

				setts["database_location"] = db

				setts2 = locations.settings()
				with open(setts2, "w") as file:
					json.dump(setts, file, indent=4)

			if root != current_root or root is not None:
				setts2 = locations.settings()
				with open(setts2, "r") as file:
					# doesnt work as one line. has to be two seperate "with opens" to modify a json.
					setts = json.load(file)

				setts["root_folder"] = root

				setts2 = locations.settings()
				with open(setts2, "w") as file:
					json.dump(setts, file, indent=4)
		elif self.flag == "dbFail":
			print("triple fail")
			messagebox.showerror("Open File", "Database is invalid.")

	def close(self):
		self.apply(self.current_theme, self.current_db, self.db, self.root, self.current_root)
		self.setts.destroy()

	def db_browse(self, mode):
		if mode == 1:
			self.db = filedialog.askopenfilename(defaultextension=".db", filetypes=[("Database", "*.db")],
													title="Choose Database")
			print(self.db)
			self.setts.db_location.insert(tkinter.INSERT, self.db)
		elif mode == 0:
			self.root = filedialog.askopenfilename(defaultextension="*", filetypes=[
													("All Files", "*.*")], title="Choose Root Folder")
			print(self.root)
			self.setts.root_location.insert(tkinter.INSERT, self.root)
		return None

	def new_user(self):
		self.setts.destroy()
		user = userCreate()


class userCreate():

	def __init__(self):
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, self.current_theme = gettheme()
		self.create = tkinter.Tk()

		# Window Creation

		relw = 30 / 192
		relh = 400 / 1080

		size = str(int((self.create.winfo_screenwidth() * (relw))))
		x = "x"
		size += x
		size += str(int(self.create.winfo_screenheight() * (relh)))

		self.create.geometry(size)
		self.create.config(bg=bg)
		self.create.iconbitmap(locations.icons() + "\\settings.ico")

		# Title:
		self.create.title("Add New User")
		self.create.titleL = tkinter.Label(self.create, text="Add New User:", foreground=text, bg=bg, font=("Verdana", 24))

		# New Username
		self.create.username = tkinter.Entry(self.create, background=box_bg, foreground=box_txt, insertbackground=cursor,
										selectbackground=select)
		self.create.userL = tkinter.Label(self.create, text="New Username:", foreground=text, bg=bg)

		# New Password
		self.create.password = tkinter.Entry(self.create, background=box_bg, foreground=box_txt,
											insertbackground=cursor, selectbackground=select, show="*")
		self.create.passwordL = tkinter.Label(self.create, text="New Password:", foreground=text, bg=bg)

		# Confirm Password
		self.create.confirm = tkinter.Entry(self.create, background=box_bg, foreground=box_txt,
		                                     insertbackground=cursor, selectbackground=select, show="*")
		self.create.confirmL = tkinter.Label(self.create, text="Confirm Password:", foreground=text, bg=bg)

		# Admin Priviledges
		self.admin_var = tkinter.BooleanVar()
		self.create.admin = tkinter.Checkbutton(self.create, variable = self.admin_var, background=bg, offvalue=False, onvalue=True)
		self.create.adminL = tkinter.Label(self.create, text="Admin Priviledges:", foreground=text, bg=bg)

		# Admin Password
		self.create.creds = tkinter.Entry(self.create, background=box_bg, foreground=box_txt,
		                                    insertbackground=cursor, selectbackground=select, show="*")
		self.create.credsL = tkinter.Label(self.create, text="Admin Password:", foreground=text, bg=bg)

		# Password Requirements
		passreqs = """
		New Passwords require at least:
		One Uppercase Character, 
		One Lowercase Character, 
		One Number and One Special Character
		"""
		self.create.reqs = tkinter.Label(self.create, text=passreqs, foreground=text, bg=bg)

		# Button
		self.create.new_user_button = tkinter.Button(self.create, text="Create New User", command=self.new_user, background=button_bg,
												foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		# Place items
		self.create.titleL.place(relx=0.5, rely=0, anchor="n")

		self.create.username.place(relx=0.375, rely=0.15, anchor="w")
		self.create.userL.place(relx=0.375, rely=0.15, anchor="e")

		self.create.password.place(relx=0.375, rely=0.225, anchor="w")
		self.create.passwordL.place(relx=0.375, rely=0.225, anchor="e")

		self.create.confirm.place(relx=0.375, rely=0.3, anchor="w")
		self.create.confirmL.place(relx=0.375, rely=0.3, anchor="e")

		self.create.admin.place(relx = 0.375, rely=0.375, anchor="w")
		self.create.adminL.place(relx=0.375, rely=0.375, anchor="e")

		self.create.creds.place(relx=0.375, rely=0.45, anchor="w")
		self.create.credsL.place(relx=0.375, rely=0.45, anchor="e")

		self.create.reqs.place(relx=0.35, rely=0.6, anchor="center")

		self.create.new_user_button.place(relx=0.5, rely=0.9, anchor="s")

		self.create.mainloop()

	def new_user(self):
		username = self.create.username.get()
		psw = self.create.password.get()
		psw2 = self.create.confirm.get()
		admin = self.admin_var.get()
		psw_admin = self.create.creds.get()

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

		print(admin)

		admin_psws = []

		for i in range(len(psws)):
			if admin[i] == "True":
				admin_psws.append(psws[i])

		flag_admin = False
		flag_unique = False
		flag_match = False
		flag_lower = False
		flag_upper = False
		flag_special = False
		flag_digits = False

		user_unique = username in users
		print(self.hash_it(psw_admin))
		print(admin_psws)
		admin_verify = self.hash_it(psw_admin) in admin_psws
		print(admin_verify)


		if admin_verify:
			flag_admin = True
		if user_unique is False:
			flag_unique = True
		if psw == psw2:
			flag_match = True

		punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

		if re.search(r'[a-z]', psw) is not None:
			flag_lower = True
		if re.search(r'[A-Z]', psw) is not None:
			flag_upper = True
		for i in range(len(punctuation)):
			if punctuation[i] in psw:
				flag_special = True
		if re.search(r'[0-9]', psw) is not None:
			flag_digits = True

		check = 0

		if flag_unique is False:
			print("Username is not unique.")
		else:
			check += 1
		if flag_match is False:
			print("Passwords do not match.")
		else:
			check += 1
		if flag_lower is False:
			print("Password does not contain lowercase letters.")
		else:
			check += 1
		if flag_upper is False:
			print("Password does not contain uppercase letters.")
		else:
			check += 1
		if flag_special is False:
			print("Password does not contain special characters.")
		else:
			check += 1
		if flag_digits is False:
			print("Password does not contain numbers.")
		else:
			check += 1
		if flag_admin is False:
			print("Admin Password is incorrect.")
		else:
			check += 1

		if check == 7:
			sql.new_user(username, self.hash_it(psw), admin)
			message = "New User was successfully created with username: "
			message += username
			tkinter.messagebox.showinfo("User Created", message)
			self.create.destroy()


	def hash_it(self, psd):
		hash = hashlib.sha512(psd.encode())
		hex = hash.hexdigest()
		return hex













def main():
	Options()
