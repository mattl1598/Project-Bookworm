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



def gettheme():
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

	return bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg

# bg,text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = self.gettheme()


class homepage:

	def __init__(self):
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		self.home = Tk()
		self.home.iconbitmap("D:\Project-Bookworm\icons\colour.ico")

		size = str(int((self.home.winfo_screenwidth()*(1280/1920))))
		x = "x"
		size += x
		size += str(int(self.home.winfo_screenheight()*(720/1080)))

		self.home.geometry(size)
		self.home.title("Project Bookworm")
		#self.home.resizable(False, False)
		self.home.configure(background=bg)
		self.randon_variable = StringVar()

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

		self.quit = Button(self.home, text="Quit", command=self.close)
		self.quit.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
								activeforeground=butt_txt)

		self.deets.place(relx=165/1280, rely=95/720, relwidth=230/1280, relheight=125/720)
		self.signOut.place(relx=405/1280, rely=95/720, relwidth=230/1280, relheight=125/720)
		self.schools.place(relx=165/1280, rely=230/720, relwidth=230/1280, relheight=125/720)
		self.settings.place(relx=645/1280, rely=500/720, relwidth=230/1280, relheight=125/720, anchor=NW)
		self.quit.place(relx=885/1280, rely=500/720, relwidth=230/1280, relheight=125/720, anchor=NW)

		self.home.mainloop()

	def book_details(self):
		self.home.destroy()
		gui.book_deets()
		# self.get2()

	def school_details(self):
		self.home.destroy()
		gui.school_details()

	def settings(self):
		self.home.destroy()
		gui.settings_menu()

	def book_sign_out(self):
		self.home.destroy()
		gui.multi_entry()

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
