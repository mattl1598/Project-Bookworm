import tkinter as Tkinter
import sqlite3
import sql
import books_api as books
import input
import book2
import json


class Form():

	def gettheme(self):
		with open("C:/Users/Matthew/Documents/GitHub/Project-Bookworm/settings.json", "r") as read2:
			settings = json.load(read2)

		rootpath = settings["root_location"]

		with open(rootpath + "theme.json", "r") as readfile:
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

	def __init__(self, text1):
		font9 = "-family {Segoe UI} -size 14 -weight normal -slant " \
				"roman -underline 0 -overstrike 0"

		bg,text, buttonBG, buttTXT, boxBG, boxTXT, cursor, select, clickedbg = self.gettheme()

		self.root = Tkinter.Tk()
		self.root.geometry("200x159+700+347")
		self.root.title("Entry Form")
		self.root.configure(background=bg)


		self.entry = Tkinter.Entry(self.root)
		self.entry.place(relx=0.08, rely=0.31, height=30, relwidth=0.82)
		self.entry.focus()
		self.entry.configure(background=boxBG, foreground=boxTXT, insertbackground=cursor, selectbackground=select)

		self.button = Tkinter.Button(self.root, text = 'Submit:', command=self.quit)
		self.button.place(relx=0.28, rely=0.63, height=44, width=87)
		self.button.configure(background=buttonBG, foreground=buttTXT, activebackground=clickedbg, activeforeground=buttTXT)

		self.Label1 = Tkinter.Label(self.root)
		self.Label1.place(relx=0.25, rely=0.06, height=31, width=99)
		self.Label1.configure(activebackground="#474747",  activeforeground="#474747", background=bg, disabledforeground="#a3a3a3",
							font=font9, foreground=text, text = text1)

		self.root.wm_attributes("-topmost", 1)
		self.root.focus_force()
		self.root.bind('<Return>', (lambda event: self.quit()))
		self.root.mainloop()

	def quit(self):
		input1 = str(self.entry.get())
		print(input1)
		isbn = input1
		self.root.destroy()

		if len(isbn) == 13 or len(isbn) == 10:
			if sql.in_db(isbn) is True:
				isbn, j, k, l, m, n, o, p, q, r = sql.get_book(isbn)
			# print(j, k, l, m, n, o, p, q, r, isbn)
			# print("sql")
			else:
				j, k, l, m, n, o, p, q, r = books.get_all_new(isbn)
				# print("books")
				print(j, k, l, m, n, o, p, q, r, isbn)
			input.bookDeets(j, k, l, m, n, o, p, q, r, isbn)
		else:
			print("error")
		#sql.dbInputIn(input1)



