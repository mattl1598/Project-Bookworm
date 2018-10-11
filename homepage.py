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
		self.home.geometry("1280x720")
		self.home.title("Project Bookworm")
		self.home.resizable(False, False)
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

		self.deets.place(x=165, y=95, width=230, height=125)
		self.signOut.place(x=405, y=95, width=230, height=125)
		self.schools.place(x=165, y=230, width=230, height=125)
		self.settings.place(x=645, y=500, width=230, height=125, anchor=NW)
		self.quit.place(x=885, y=500, width=230, height=125, anchor=NW)

		self.home.mainloop()

	def book_details(self):
		self.home.destroy()
		input1.isbn2book()
		# self.get2()

	def school_details(self):
		self.home.destroy()
		schoolDetails.start()

	def settings(self):
		self.home.destroy()
		settings.main()

	def book_sign_out(self):
		self.home.destroy()
		multientry.class3()

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
