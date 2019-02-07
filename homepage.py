from tkinter import *
from tkinter import StringVar
import input as input1
import json
import settings
import time
import multientry
import requests
import urllib.request
import os
import schoolDetails
import gui
import sql
from win32com.shell import shell, shellcon

def gettheme():
	docs = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
	setts = docs + "\\GitHub\\Project-Bookworm\\settings.json"
	with open(setts, "r") as read2:
		settings = json.load(read2)

	rootpath = settings["root_location"]

	with open(rootpath+"theme.json", "r") as readfile:
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


	return bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, rootpath

# bg,text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = self.gettheme()


class homepage:

	def __init__(self):
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, rootpath = gettheme()

		with open("C:/Users/Matthew/Documents/GitHub/Project-Bookworm/settings.json", "r") as readfile:
			settings = json.load(readfile)

		logins = sql.get_logins()

		ids = []
		users = []
		psws = []
		for i in range(len(logins)):
			ids.append(str(logins[i][0]))
			users.append(logins[i][1])
			psws.append(logins[i][2])

		user_id = settings["last_user_id"]
		if str(user_id) in ids:
			user = users[ids.index(str(user_id))]
			welc_string = "Welcome back, "
			welc_string += user
			welc_string += "!"
		else:
			welc_string = "Welcome Back!"

		self.home = Tk()
		self.home.iconbitmap(rootpath+"icons\colour.ico")

		size = str(int((self.home.winfo_screenwidth()*(1280/1920))))
		x = "x"
		size += x
		size += str(int(self.home.winfo_screenheight()*(720/1080)))

		self.home.geometry(size)
		self.home.title("Project Bookworm")
		self.home.resizable(False, False)
		self.home.configure(background=bg)
		self.randon_variable = StringVar()

		self.welc = Label(self.home)
		self.welc.config(activebackground=bg, activeforeground=text, background=bg, foreground=text,
								highlightbackground=bg, text=welc_string, font=("Verdana", 24))

		self.deets = Button(self.home, text="Book Details", command=self.book_details)
		self.deets.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
								activeforeground=butt_txt)

		self.signOut = Button(self.home, text="Sign out Books", command=self.book_sign_out)
		self.signOut.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
								activeforeground=butt_txt)

		self.schools = Button(self.home, text="School Details", command=self.school_details)
		self.schools.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
								activeforeground=butt_txt)

		self.settings = Button(self.home, text="Settings", command=self.settings)
		self.settings.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
								activeforeground=butt_txt)

		self.logoff = Button(self.home, text="Log Out", command=self.logout)
		self.logoff.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
		                    activeforeground=butt_txt)

		self.quit = Button(self.home, text="Quit", command=self.close)
		self.quit.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
								activeforeground=butt_txt)

		self.deets.place(relx=165/1280, rely=95/720, relwidth=230/1280, relheight=125/720)
		self.signOut.place(relx=405/1280, rely=95/720, relwidth=230/1280, relheight=125/720)
		self.schools.place(relx=165/1280, rely=230/720, relwidth=230/1280, relheight=125/720)
		self.settings.place(relx=645/1280, rely=500/720, relwidth=230/1280, relheight=125/720, anchor=NW)
		self.logoff.place(relx=885 / 1280, rely=365 / 720, relwidth=230 / 1280, relheight=125 / 720, anchor=NW)
		self.quit.place(relx=885/1280, rely=500/720, relwidth=230/1280, relheight=125/720, anchor=NW)
		self.welc.place(relx=640/1280, rely=672/720, anchor=CENTER)

		self.home.mainloop()

	def book_details(self):
		self.home.destroy()
		gui.book_deets()

	def school_details(self):
		self.home.destroy()
		gui.school_details()

	def settings(self):
		self.home.destroy()
		gui.settings_menu()

	def book_sign_out(self):
		self.home.destroy()
		gui.multi_entry()

	def logout(self):
		self.close()
		gui.logins()

	def close(self):
		self.home.destroy()

	def get_isbn(self):
		proxy_dict = {
			'http': 'http://proxy.rmplc.co.uk:8080',
			'https': 'https://proxy.rmplc.co.uk:8080'
		}
		i = input("isbn")
		self.random_variable.set(i)
		u = "https://www.googleapis.com/books/v1/volumes?q="
		u += i
		r = requests.get(u, proxies=proxy_dict)
		print(r.json())

	def get2(self):
		assert 'SYSTEMROOT' in os.environ
		i = input("isbn")
		self.random_variable.set(i)
		u = "https://www.googleapis.com/books/v1/volumes?q="
		u += i
		r = urllib.request.urlopen(u).read()
		print(r)


def main():
	menu = homepage()
