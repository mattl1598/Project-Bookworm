import tkinter
import json
import books_api as books
import sql
import sqlite3
import misc_python


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



class Selection:

	def __init__(self):

		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		self.root = tkinter.Tk()
		self.root.title("Signing")
		self.root.geometry("400x300")
		self.root.configure(background=bg)

		self.school = tkinter.StringVar(self.root)

		self.location = None

		self.lookup, self.lookup2, schools = sql.get_schools()
		self.schools = schools

		self.root.location = tkinter.OptionMenu(self.root, self.school, *schools)

		self.root.location.config(background=button_bg, foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt,
									highlightthickness=0, highlightcolor=bg, highlightbackground=bg)

		self.root.location["menu"].config(bg=button_bg, foreground=butt_txt, bd="0", activebackground="SystemHighlight",
											activeforeground=butt_txt)

		self.root.sign_inB = tkinter.Button(self.root, command=self.sign_in, text="Sign in", background=button_bg,
											foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.root.sign_outB = tkinter.Button(self.root, command=self.sign_out, text="Sign Out", background=button_bg,
												foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.root.location.place(relx=0.5, rely=0.4, anchor="n")

		self.root.sign_inB.place(relx=0.45, rely=0.7, anchor="e")
		self.root.sign_outB.place(relx=0.55, rely=0.7, anchor="w")

		self.root.mainloop()

	def sign_in(self):
		loc = self.get_location()
		self.root.destroy()
		app = App(0, loc)

	def sign_out(self):
		loc = self.get_location()
		self.root.destroy()
		app = App(1, loc)

	def get_location(self):
		school_name = self.school.get()
		school_id = self.lookup[school_name]
		return school_id


class App:
	def __init__(self, mode, loc):

		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		self.mode = mode
		self.location = loc

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

		self.root.submit = tkinter.Button(self.root, background=button_bg,
											foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)
		if self.mode == 1:
			self.root.submit.config(text="Sign Out", command=lambda: self.submit("out"))
		elif self.mode == 0:
			self.root.submit.config(text="Sign In", command=lambda: self.submit("in"))

		# fill the listboxes with stuff
		# for x in range(300):
		# 	self.root.list1.insert('end', x)
		# 	self.root.list2.insert('end', x)

		self.root.entry = tkinter.Entry(self.root)
		self.root.entry.config(background=box_bg, foreground=box_txt, insertbackground=cursor, selectbackground=select)
		self.root.entry.focus()
		self.root.entry.place(anchor="center", relx=0.5, rely=0.6)
		self.root.bind('<Return>', (lambda event: self.add_isbn()))

		self.root.submit.place(relx=0.5, rely=0.7, anchor="n")

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
		if len(isbn) == 13 or len(isbn) == 10:
			if sql.in_db(isbn) is True:
				isbn, title, k, l, m, n, o, p, q, r = sql.get_book(isbn)
				# print(j, k, l, m, n, o, p, q, r, isbn)
				# print("sql")
				self.root.ISBNs.append(isbn)
				self.root.list1.insert('end', isbn)
				self.root.list2.insert("end", title)
			elif books.getNewBook(isbn) != {'kind': 'books#volumes', 'totalItems': 0} and sql.in_db(isbn) is False:
				title = books.get_single_deet(isbn, "title")
				# print("books")
				self.root.ISBNs.append(isbn)
				self.root.list1.insert('end', isbn)
				self.root.list2.insert("end", title)
			else:
				print("error")
		else:
			print("error")

	def submit(self, mode):
		print(self.location)
		if mode == "in":
			if self.location == 0:
				for i in range(len(self.root.ISBNs)):
					isbn = self.root.ISBNs[i]
					db = sql.get_db()
					conn = sqlite3.connect(db)
					c = conn.cursor()
					cmd = "select copy_no from books where isbn = ?"
					c.execute(cmd, (isbn,))
					data = c.fetchall()

					new_data = []

					for i in range(len(data)):
						new_data.append(list(data[i])[0])

					sorted_data = sorted(new_data)
					print(sorted_data)
					if sorted_data == []:
						new_copy_no = 1
					else:
						highest_copy = sorted_data[len(sorted_data)-1]
						new_copy_no = highest_copy + 1
					print(new_copy_no)
					cmd2 = "insert into books(isbn, copy_no, loan_id) values(?,?,?)"
					try:
						c.execute(cmd2, (isbn, new_copy_no, 0,))
					except sqlite3.IntegrityError:
						c.execute(cmd2, (isbn, new_copy_no + 1, 0,))
					conn.commit()
					conn.close()
			else:
				pass
		elif mode == "out":
			books = sql.get_books_location(0)
			sql.create_new_loan(self.location)
			for i in range(len(self.root.ISBNS)):
				isbn = self.root.ISBNs[i]
				copy = sql.get_copys_location(0, isbn)
				copy_list = []
				for j in range(len(copy)):
					copy_list.append(copy[i][1])
					copy_list = sorted(copy_list)
				if copy_list == []:
					pass # error plz
				else:
					copy_no = copy_list[0]
					if self.location == "0":
						pass # delete these
					else:
						loan_id = sql.create_new_loan(self.location)
						print(loan_id)
						pass
						# loan_id =




def class3():
	selection = Selection()
