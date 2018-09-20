from tkinter import *
import input
import json
import settings
import time
import multientry




class homepage():

	def gettheme(self):
		with open("D:/Project-Bookworm/theme.json", "r") as readfile:
			theme1 = json.load(readfile)

		theme = theme1["theme"]

		bg = theme1[theme]["windows"]["background"]
		text = theme1[theme]["windows"]["text"]
		buttonBG = theme1[theme]["button"]["background"]
		buttTXT = theme1[theme]["button"]["text"]
		boxBG = theme1[theme]["textbox"]["background"]
		boxTXT = theme1[theme]["textbox"]["foreground"]
		cursor = theme1[theme]["textbox"]["insertbackground"]
		select = theme1[theme]["textbox"]["selectbackground"]
		clickedbg = theme1[theme]["button"]["clickedbg"]

		return bg, text, buttonBG, buttTXT, boxBG, boxTXT, cursor, select, clickedbg
		#bg,text, buttonBG, buttTXT, boxBG, boxTXT, cursor, select, clickedbg = self.gettheme()

	def __init__(self):
		bg,text, buttonBG, buttTXT, boxBG, boxTXT, cursor, select, clickedbg = self.gettheme()

		#time.sleep(10)


		self.home = Tk()
		self.home.geometry("1280x720")
		self.home.title("Project Bookworm")
		self.home.resizable(False, False)
		self.home.configure(background=bg)

		self.deets = Button(self.home, text="Book Details", command=self.bookDetails)
		self.deets.configure(background=buttonBG, foreground=buttTXT, activebackground=clickedbg, activeforeground=buttTXT)

		self.signOut = Button(self.home, text="Sign out Books", command=self.bookSignOut)
		self.signOut.configure(background=buttonBG, foreground=buttTXT, activebackground=clickedbg, activeforeground=buttTXT)

		self.settings = Button(self.home, text="Settings", command=self.settings)
		self.settings.configure(background=buttonBG, foreground=buttTXT, activebackground=clickedbg, activeforeground=buttTXT)

		self.quit = Button(self.home, text="Quit", command=self.close)
		self.quit.configure(background=buttonBG, foreground=buttTXT, activebackground=clickedbg, activeforeground=buttTXT)

		self.deets.place(x=165, y=95, width=230, height=125)
		self.signOut.place(x=405, y=95, width=230, height=125)
		self.settings.place(x=645, y=500, width=230, height=125, anchor=NW)
		self.quit.place(x=885, y=500, width=230, height=125, anchor=NW)

		self.home.mainloop()

	def bookDetails(self):
		self.home.destroy()
		input.isbn2book()

	def settings(self):
		self.home.destroy()
		settings.main()

	def bookSignOut(self):
		self.home.destroy()
		multientry.class3()

	def close(self):
		self.home.destroy()


def main():
	menu = homepage()