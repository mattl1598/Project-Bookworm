import tkinter
import locations
import json
import sql
import misc_python as misc
import books_api as books
import tkinter.ttk as ttk
import time
import xlsxwriter
import datetime


def gettheme():
	setts = locations.settings()
	with open(setts, "r") as read2:
		setting = json.load(read2)

	rootpath = setting["root_location"]

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

	return bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg

# bg,text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = self.gettheme()


class Generator:

	def __init__(self):

		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()
		self.root = tkinter.Tk()
		self.root.geometry("300x400")
		self.root.configure(background=bg)

		self.root.loc = tkinter.Label(self.root, foreground=text, bg=bg, text="Location")

		self.school = tkinter.StringVar(self.root)
		self.lookup, self.lookup2, schools = sql.get_schools()
		self.root.loc_drop = tkinter.OptionMenu(self.root, self.school, *schools, command=self.change_drop3)

		self.root.loc_drop.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
									activeforeground=butt_txt, highlightthickness=0, highlightcolor=bg,
									highlightbackground=bg)
		self.root.loc_drop["menu"].config(bg=button_bg, foreground=butt_txt, bd="0", activebackground="SystemHighlight",
										activeforeground=butt_txt)

		self.root.report_type = tkinter.Label(self.root, foreground=text, bg=bg, text="Report type")
		self.report = tkinter.StringVar(self.root)
		reports = misc.better_sort(["List of Books", "Stock Numbers", "List of Books Marked as Lost", "Allocation Stats",
									"Unique Titles over Time", "List of Visits"])
		self.root.report_drop = tkinter.OptionMenu(self.root, self.report, *reports, command=self.change_drop2)

		self.root.report_drop.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
										activeforeground=butt_txt, highlightthickness=0, highlightcolor=bg,
										highlightbackground=bg)
		self.root.report_drop["menu"].config(bg=button_bg, foreground=butt_txt, bd="0", activebackground="SystemHighlight",
												activeforeground=butt_txt)

		self.root.report_type.place(relx=3 / 10, rely=2 / 10, anchor="e")
		self.root.report_drop.place(relx=3 / 10, rely=2 / 10, anchor="w")

		self.root.submit = tkinter.Button(self.root, command=self.button, text="Generate Report", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.root.quit = tkinter.Button(self.root, command=self.quit, text="Close", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.root.quit.place(relx=3/5, rely=9/10, anchor="w")

		self.root.mainloop()

	def change_drop2(self, report):

		if report == "List of Books" or report == "List of Visits":
			self.root.loc.place(relx=3 / 10, rely=4 / 10, anchor="e")
			self.root.loc_drop.place(relx=3 / 10, rely=4 / 10, anchor="w")
			self.hide_button()
		else:
			self.root.loc.place_forget()
			self.root.loc_drop.place_forget()
			self.school.set("")
			self.show_button()

	def change_drop3(self, loc):
		report = self.report.get()

		self.show_button()

	def show_button(self):
		self.root.submit.place(relx=2 / 5, rely=9 / 10, anchor="center")

	def hide_button(self):
		self.root.submit.place_forget()

	def button(self):
		# print("Generated!")
		self.root.destroy()
		if self.report.get() == "List of Books":
			school_id = self.lookup[self.school.get()]
			loan_id = sql.get_loans(school_id)
			isbns = []
			for i in range(len(loan_id)):
				isbns2 = sql.get_books_from_loan(loan_id[i])
				for c in range(len(isbns2)):
					isbns.append(isbns2[c])
			report = BookList(isbns, self.school.get())
		elif self.report.get() == "Allocation Stats":
			report = AllocStats()
		elif self.report.get() == "List of Books Marked as Lost":
			isbns = sql.get_lost_books()
			report = LostBooks(isbns)
		main()

	def quit(self):
		self.root.destroy()


class AllocStats:

	def sort_column(self, table, col, reverse):
		l = [(table.set(k, col), k) for k in table.get_children('')]
		try:
			l.sort(key=lambda t: int(t[0]), reverse=reverse)
		except ValueError:
			l.sort(reverse=reverse)

		for index, (val, k) in enumerate(l):
			table.move(k, '', index)

		table.heading(col, command=(lambda: self.sort_column(table, col, not reverse)))

	def __init__(self):
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		self.lookup, self.lookup2, schools = sql.get_schools()

		schools.pop(schools.index("Base"))

		popup = tkinter.Tk()
		popup.geometry("300x100")
		popup.config(background=bg)
		progress = 0
		progress_var = tkinter.DoubleVar()
		progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=(len(schools)-1))
		progress_bar.place(relx=0.5, rely=0.5, anchor="center")  # .pack(fill=tk.X, expand=1, side=tk.BOTTOM)
		popup.pack_slaves()
		progress_step = float(1)

		sch = []
		totals = []
		alloc = []
		over = []

		for school in schools:
			popup.update()
			school_id = self.lookup[school]
			loan_id = sql.get_loans(school_id)
			isbns = []
			for i in range(len(loan_id)):
				isbns2 = sql.get_books_from_loan(loan_id[i])
				for c in range(len(isbns2)):
					isbns.append(isbns2[c])
			book_total = len(isbns)
			progress += progress_step
			progress_var.set(progress)
			time.sleep(0.1)
			sch.append(school)
			totals.append(book_total)
			data = sql.get_school_deets(school_id)
			alloc1 = int(data["itemsPer"]) * int(data["pupilTotal"])
			alloc.append(alloc1)
			if book_total > alloc1:
				over.append("Over")
			elif book_total < alloc1:
				over.append("Under")
			elif book_total == alloc1:
				over.append("On")

			# print(school, book_total)

		popup.destroy()

		self.AllocStats = tkinter.Tk()
		self.AllocStats.geometry("516x600")
		self.AllocStats.title("Allocation Statistics")
		self.AllocStats.config(background=bg)

		columns = ("School", "Current Books", "Allocation", "Over or Under",)
		self.AllocStats.scroll_bar = tkinter.Scrollbar(self.AllocStats)
		self.AllocStats.table = ttk.Treeview(self.AllocStats, columns=columns, show='headings',
												yscrollcommand=self.AllocStats.scroll_bar.set)
		self.AllocStats.table.tag_configure('colour', background=box_bg, foreground=box_txt)
		'''
		self.AllocStats.table.heading("#0", text="School")
		self.AllocStats.table.heading("#1", text="Current Books")
		self.AllocStats.table.heading("#2", text="Allocation")
		self.AllocStats.table.heading("#3", text="Over or Under")
		'''
		self.AllocStats.table.column("#1", width=250)
		self.AllocStats.table.column("#2", width=80)
		self.AllocStats.table.column("#3", width=60)
		self.AllocStats.table.column("#4", width=80)

		for i in range(len(sch)):
			self.AllocStats.table.insert("", index="end", values=(sch[i], totals[i], alloc[i], over[i],), tags=('colour',))

		for col in columns:
			self.AllocStats.table.heading(col, text=col, command=lambda c=col: self.sort_column(self.AllocStats.table, c, False))

		# print(sch[i], totals[i], alloc[i], over[i])

		self.AllocStats.print = tkinter.Button(self.AllocStats, command=self.print, text="Print", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.AllocStats.close = tkinter.Button(self.AllocStats, command=self.AllocStats.destroy, text="Close", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.AllocStats.table.place(x=0, y=0, width=500, height=500, anchor="nw")
		self.AllocStats.scroll_bar.place(x=516, y=0, height=500, anchor="ne")
		self.AllocStats.scroll_bar.config(command=self.AllocStats.table.yview)
		self.AllocStats.print.place(x=250, y=550, anchor="e")
		self.AllocStats.close.place(x=282, y=550, anchor="w")
		self.AllocStats.mainloop()

	def get_total_items(self):
		item = 1
		flag = True

		while flag:
			hex_item = hex(item)[2:].upper()
			length = len(hex_item)
			for i in range(3 - length):
				hex_item = "0" + hex_item
			hex_item = "I" + hex_item
			# print(hex_item)
			try:
				value = self.AllocStats.table.item(hex_item)['values']
				item += 1
			except tkinter.TclError:
				flag = False
		# print(item)
		return item

	def print2(self):
		total = self.get_total_items() -1
		start = self.AllocStats.table.identify("item", 20, 36)
		# print(start2)
		flag = True
		item = 1
		values = []
		# start = self.AllocStats.table.focus()
		while flag:
			try:
				value = self.AllocStats.table.item(start)['values']
				# print(value)
				values.append(value)
				start = self.AllocStats.table.next(start)
				item += 1
				if item > total:
					flag = False
			except tkinter.TclError:
				flag = False
		return values

	def print(self):
		self.create_printout()

	def create_printout(self):
		values = self.print2()
		docs = locations.docs()
		workbook = xlsxwriter.Workbook(docs + "\\Project-Bookworm\\Reports\\Allocation " + str(
			datetime.datetime.now().strftime("%d-%m-%Y %H-%M")) + ".xlsx")
		worksheet = workbook.add_worksheet("Allocation")

		worksheet.set_column('A:A', 40)
		worksheet.set_column('B:D', 10)
		for i in range(len(values)):
			worksheet.write(i, 0, values[i][0])
			worksheet.write(i, 1, values[i][1])
			worksheet.write(i, 2, values[i][2])
			worksheet.write(i, 3, values[i][3])
		workbook.close()


class BookList:

	def sort_column(self, table, col, reverse):
		l = [(table.set(k,col),k) for k in table.get_children('')]
		try:
			l.sort(key=lambda t: int(t[0]), reverse=reverse)
		except ValueError:
			l.sort(reverse=reverse)

		for index, (val, k) in enumerate(l):
			table.move(k, '', index)

		table.heading(col, command=(lambda: self.sort_column(table, col, not reverse)))

	def __init__(self, isbns, school):

		self.school = school
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		popup = tkinter.Tk()
		popup.geometry("300x100")
		popup.config(background=bg)
		progress = 0
		progress_var = tkinter.DoubleVar()
		progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=len(isbns)-1)
		progress_bar.place(relx=0.5, rely=0.5, anchor="center")  # .pack(fill=tk.X, expand=1, side=tk.BOTTOM)
		# print(isbns)
		isbns2 = []
		titles = []
		quantity = []
		popup.pack_slaves()
		progress_step = float(1)
		for i in range(len(isbns)):
			popup.update()
			if sql.in_db(isbns[i]) is True:
				isbn, j, k, l, m, n, o, p, q, r = sql.get_book(isbns[i])
			# print(j, k, l, m, n, o, p, q, r, isbn)
			# print("sql")
			else:
				j = books.get_single_deet(isbns[i], "title")
			# print("books")
			# print(j, k, l, m, n, o, p, q, r, isbns[i])
			temp = j.rstrip("\n\r")
			try:
				pos = isbns2.index(isbns[i])
			except ValueError:
				isbns2.append(isbns[i])
				titles.append(temp)
				quantity.append("1")
				# print(titles)
			else:
				new_quant = int(quantity[pos]) + int(1)
				quantity[pos] = new_quant
			# titles.append(j.rstrip("\n\r"))
			progress += progress_step
			progress_var.set(progress)
		popup.destroy()

		# print(len(isbns2), len(titles), len(quantity))

		self.BookList = tkinter.Tk()
		self.BookList.geometry("516x400")
		self.BookList.title(school)
		self.BookList.config(background=bg)

		columns = ("ISBN", "Title", "Quantity",)

		self.BookList.scroll_bar = tkinter.Scrollbar(self.BookList)
		self.BookList.print = tkinter.Button(self.BookList, command=self.print, text="Print", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)
		self.BookList.close = tkinter.Button(self.BookList, command=self.BookList.destroy, text="Close", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.BookList.table = ttk.Treeview(self.BookList, columns=columns, show='headings',
											yscrollcommand=self.BookList.scroll_bar.set, )
		self.BookList.table.tag_configure('colour', background=box_bg, foreground=box_txt)

		self.BookList.table.column("#1", width=100, anchor="w")
		self.BookList.table.column("#2", width=330)
		self.BookList.table.column("#3", width=70)

		for i in range(0, len(titles)):
			self.BookList.table.insert("", index="end", values=(isbns2[i].rstrip("\n\r"), titles[i], quantity[i],),
										tags=('colour',))

		for col in columns:
			self.BookList.table.heading(col, text=col, command=lambda c=col: self.sort_column(self.BookList.table, c, False))

		self.BookList.table.place(x=0, y=0, width=500, height=300, anchor="nw")
		self.BookList.print.place(x=250, y=350, anchor="e")
		self.BookList.close.place(x=282, y=350, anchor="w")
		self.BookList.scroll_bar.place(x=516, y=0, height=300, anchor="ne")
		self.BookList.scroll_bar.config(command=self.BookList.table.yview)

		self.BookList.mainloop()

	def get_total_items(self):
		item = 1
		flag = True

		while flag:
			hex_item = hex(item)[2:].upper()
			length = len(hex_item)
			for i in range(3 - length):
				hex_item = "0" + hex_item
			hex_item = "I" + hex_item
			# print(hex_item)
			try:
				value = self.BookList.table.item(hex_item)['values']
				item += 1
			except tkinter.TclError:
				flag = False
		# print(item)
		return item

	def print2(self):
		total = self.get_total_items() -1
		start = self.BookList.table.identify("item", 20, 36)
		# print(start2)
		flag = True
		item = 1
		values = []
		# start = self.AllocStats.table.focus()
		while flag:
			try:
				value = self.BookList.table.item(start)['values']
				# print(value)
				values.append(value)
				start = self.BookList.table.next(start)
				item += 1
				if item > total:
					flag = False
			except tkinter.TclError:
				flag = False
		return values

	def print(self):
		self.create_printout()

	def create_printout(self):
		values = self.print2()
		docs = locations.docs()
		workbook = xlsxwriter.Workbook(docs + "\\Project-Bookworm\\Reports\\Books at " + self.school.rstrip("\n\r") + " " + str(
			datetime.datetime.now().strftime("%d-%m-%Y %H-%M")) + ".xlsx")
		worksheet = workbook.add_worksheet(self.school)

		cell_format = workbook.add_format()
		cell_format.set_num_format('0')

		worksheet.set_column('A:A', 20)
		worksheet.set_column('B:B', 40)
		worksheet.set_column('C:C', 10)
		for i in range(len(values)):
			worksheet.write(i, 0, values[i][0], cell_format)
			worksheet.write(i, 1, values[i][1])
			worksheet.write(i, 2, values[i][2])
		workbook.close()


class LostBooks:

	def __init__(self, isbns):

		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		popup = tkinter.Tk()
		popup.geometry("300x100")
		popup.config(background=bg)
		progress = 0
		progress_var = tkinter.DoubleVar()
		progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=len(isbns)-1)
		progress_bar.place(relx=0.5, rely=0.5, anchor="center")  # .pack(fill=tk.X, expand=1, side=tk.BOTTOM)
		# print(isbns)
		isbns2 = []
		titles = []
		quantity = []
		popup.pack_slaves()
		progress_step = float(1)
		for i in range(len(isbns)):
			popup.update()
			if sql.in_db(isbns[i]) is True:
				isbn, j, k, l, m, n, o, p, q, r = sql.get_book(isbns[i])
			# print(j, k, l, m, n, o, p, q, r, isbn)
			# print("sql")
			else:
				j = books.get_single_deet(isbns[i], "title")
			# print("books")
			# print(j, k, l, m, n, o, p, q, r, isbns[i])
			temp = j.rstrip("\n\r")
			try:
				pos = isbns2.index(isbns[i])
			except ValueError:
				isbns2.append(isbns[i])
				titles.append(temp)
				quantity.append("1")
				# print(titles)
			else:
				new_quant = int(quantity[pos]) + int(1)
				quantity[pos] = new_quant
			# titles.append(j.rstrip("\n\r"))
			progress += progress_step
			progress_var.set(progress)
		popup.destroy()

		# print(len(isbns2), len(titles), len(quantity))

		self.LostBooks = tkinter.Tk()
		self.LostBooks.geometry("516x400")
		self.LostBooks.title("Lost Books")
		self.LostBooks.config(background=bg)

		self.LostBooks.print = tkinter.Button(self.LostBooks, command=self.print, text="Print", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)
		self.LostBooks.close = tkinter.Button(self.LostBooks, command=self.LostBooks.destroy, text="Close", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.LostBooks.table = ttk.Treeview(self.LostBooks, columns=("isbn", "title", "quant",), show='headings')
		self.LostBooks.table.tag_configure('colour', background=box_bg, foreground=box_txt)
		self.LostBooks.table.heading("#1", text="ISBN")
		self.LostBooks.table.heading("#2", text="Title")
		self.LostBooks.table.heading("#3", text="Quantity")
		self.LostBooks.table.column("#1", width=100, anchor="w")
		self.LostBooks.table.column("#2", width=330)
		self.LostBooks.table.column("#3", width=70)

		for i in range(0, len(titles)):
			self.LostBooks.table.insert("", index="end", values=(isbns2[i].rstrip("\n\r"), titles[i], quantity[i],), tags=('colour',))

		self.LostBooks.table.place(x=0, y=0, width=500, height=300, anchor="nw")
		self.LostBooks.print.place(x=250, y=350, anchor="e")
		self.LostBooks.close.place(x=282, y=350, anchor="w")

		self.LostBooks.mainloop()

	def get_total_items(self):
		item = 1
		flag = True

		while flag:
			hex_item = hex(item)[2:].upper()
			length = len(hex_item)
			for i in range(3 - length):
				hex_item = "0" + hex_item
			hex_item = "I" + hex_item
			# print(hex_item)
			try:
				value = self.LostBooks.table.item(hex_item)['values']
				item += 1
			except tkinter.TclError:
				flag = False
		# print(item)
		return item

	def print2(self):
		total = self.get_total_items() -1
		start = self.LostBooks.table.identify("item", 20, 36)
		# print(start2)
		flag = True
		item = 1
		values = []
		# start = self.AllocStats.table.focus()
		while flag:
			try:
				value = self.LostBooks.table.item(start)['values']
				# print(value)
				values.append(value)
				start = self.LostBooks.table.next(start)
				item += 1
				if item > total:
					flag = False
			except tkinter.TclError:
				flag = False
		return values

	def print(self):
		self.create_printout()

	def create_printout(self):
		values = self.print2()
		docs = locations.docs()
		workbook = xlsxwriter.Workbook(docs + "\\Project-Bookworm\\Reports\\Lost Books "+ str(
			datetime.datetime.now().strftime("%d-%m-%Y %H-%M")) + ".xlsx")
		worksheet = workbook.add_worksheet("Lost Books")

		cell_format = workbook.add_format()
		cell_format.set_num_format('0')

		worksheet.set_column('A:A', 20)
		worksheet.set_column('B:B', 40)
		worksheet.set_column('C:C', 10)
		for i in range(len(values)):
			worksheet.write(i, 0, values[i][0], cell_format)
			worksheet.write(i, 1, values[i][1])
			worksheet.write(i, 2, values[i][2])
		workbook.close()

def main():
	app = Generator()


if __name__ == "__main__":
	main()
