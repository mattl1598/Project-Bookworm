import tkinter
import homepage
import json
from tkinter import filedialog
from tkinter import messagebox
from IPy import IP
import sqlite3



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


class Options:

	def __init__(self):

		# import colours
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, self.current_theme = gettheme()

		with open("D:/Project-Bookworm/settings.json", "r") as readfile:
			setts = json.load(readfile)

		self.current_db = setts["database_location"]
		self.current_root = setts["root_location"]
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
		self.setts.iconbitmap("D:\Project-Bookworm\icons\settings.ico")
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

		print(self.themeDrop)
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
				flag = True
			except sqlite3.OperationalError:
				print("double fail")
				self.flag = "dbFail"

		if self.flag != "dbFail":
			if theme != current_theme:

				with open("D:/Project-Bookworm/theme.json", "r") as file:
					# doesnt work as one line. has to be two seperate "with opens" to modify a json.
					theme1 = json.load(file)

				theme1["theme"] = theme

				with open("D:/Project-Bookworm/theme.json", "w") as file:
					json.dump(theme1, file, indent=4)

			if db != current_db or db is not None:

				with open("D:/Project-Bookworm/settings.json", "r") as file:
					# doesnt work as one line. has to be two seperate "with opens" to modify a json.
					setts = json.load(file)

				setts["database_location"] = db

				with open("D:/Project-Bookworm/settings.json", "w") as file:
					json.dump(setts, file, indent=4)

			if root != current_root or root is not None:

				with open("D:/Project-Bookworm/settings.json", "r") as file:
					# doesnt work as one line. has to be two seperate "with opens" to modify a json.
					setts = json.load(file)

				setts["root_folder"] = root

				with open("D:/Project-Bookworm/settings.json", "w") as file:
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


def main():
	Options()
