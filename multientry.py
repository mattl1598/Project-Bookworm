<<<<<<< HEAD
import tkinter
import json
import books_api as books
import sql


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


class App:

	def __init__(self):

		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		self.root = tkinter.Tk()
		self.root.title("Test")
		self.root.geometry("1024x576")
		# self.root.resizable(0,0)
		self.root.configure(background=bg)

		self.root.ISBNs = []

		# scrollbar
		self.root.scrollbar = tkinter.Scrollbar(self.root)
		self.root.scrollbar.pack(side="right", fill="y")

		# note that yscrollcommand is set to a custom method for each listbox
		self.root.list1 = tkinter.Listbox(self.root, yscrollcommand=self.yscroll1)
		self.root.list1.place(x=170, y=95, width=337, height=150)
		self.root.list1.config(background=box_bg, foreground=box_txt, bd=0, justify="right")

		self.root.list2 = tkinter.Listbox(self.root, yscrollcommand=self.yscroll2)
		self.root.list2.place(x=517, y=95, width=337, height=150)
		self.root.list2.config(background=box_bg, foreground=box_txt)

		self.root.scrollbar.config(command=self.yview)
		self.root.scrollbar.place(x=1031, y=95, height=150)

		# fill the listboxes with stuff
		# for x in range(300):
		# 	self.root.list1.insert('end', x)
		# 	self.root.list2.insert('end', x)

		self.root.entry = tkinter.Entry(self.root)
		self.root.entry.config(background=box_bg, foreground=box_txt, insertbackground=cursor, selectbackground=select)
		self.root.entry.focus()
		self.root.entry.place(anchor="center", relx=0.5, rely=0.6)
		self.root.bind('<Return>', (lambda event: self.add_isbn()))

		self.root.mainloop()

	def yscroll1(self, *args):
		if self.root.list2.yview() != self.root.list1.yview():
			self.root.list2.yview_moveto(args[0])
		self.root.scrollbar.set(*args)

	def yscroll2(self, *args):
		if self.root.list1.yview() != self.root.list2.yview():
			self.root.list1.yview_moveto(args[0])
		self.root.scrollbar.set(*args)

	def yview(self, *args):
		self.root.list1.yview(*args)
		self.root.list2.yview(*args)

	def add_isbn(self):
		isbn = str(self.root.entry.get())
		self.root.entry.delete(0, "end")
		self.root.ISBNs.append(isbn)
		self.root.list1.insert('end', isbn)

		# what the fuck is wrong with this code
		# title = books.getTitle(books.getBook(input1))

		if len(isbn) == 13 or len(isbn) == 10:
			if sql.in_db(isbn) is True:
				isbn, title, k, l, m, n, o, p, q, r = sql.get_book(isbn)
			# print(j, k, l, m, n, o, p, q, r, isbn)
			# print("sql")
			else:
				title = books.getTitle(books.getBook(isbn))
				# print("books")
			self.root.list2.insert("end", title)
		else:
			print("error")


def class3():
	app = App()
=======
import tkinter
import json

class App():

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

		self.root = tkinter.Tk()
		self.root.title("Test")
		self.root.geometry("1024x576")
		self.root.resizable(0,0)
		self.root.configure(background=bg)

		#scrollbar
		self.root.scrollbar = tkinter.Scrollbar(self.root)
		self.root.scrollbar.pack(side="right", fill="y")

		# note that yscrollcommand is set to a custom method for each listbox
		self.root.list1 = tkinter.Listbox(self.root, yscrollcommand=self.yscroll1)
		self.root.list1.place(x=165, y=95, width=337, height=150)
		self.root.list1.config(background=boxBG, foreground=boxTXT, bd=0)

		self.root.list2 = tkinter.Listbox(self.root, yscrollcommand=self.yscroll2)
		self.root.list2.place(x=512, y=95, width=320, height=150)
		self.root.list2.config(background=boxBG, foreground=boxTXT)

		self.root.scrollbar.config(command=self.yview)
		self.root.scrollbar.place(x=1031, y=95, height=150)

		# fill the listboxes with stuff
		for x in range(300):
			self.root.list1.insert('end', x)
			self.root.list2.insert('end', x)

		self.root.mainloop()

	def yscroll1(self, *args):     #1509860142
		if self.root.list2.yview() != self.root.list1.yview():
			self.root.list2.yview_moveto(args[0])
		self.root.scrollbar.set(*args)

	def yscroll2(self, *args):
		if self.root.list1.yview() != self.root.list2.yview():
			self.root.list1.yview_moveto(args[0])
		self.root.scrollbar.set(*args)

	def yview(self, *args):
		self.root.list1.yview(*args)
		self.root.list2.yview(*args)

def class3():
	app = App()

>>>>>>> 77d70087116cb3542db994ff5dd771921a03de6f
