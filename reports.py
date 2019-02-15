import tkinter
from win32com.shell import shell, shellcon
import json
import sql
import misc_python as misc
import books_api as books
import tkinter.ttk as ttk
import time


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

		self.root.report_type.place(relx=2 / 5, rely=2 / 10, anchor="e")
		self.root.report_drop.place(relx=2 / 5, rely=2 / 10, anchor="w")

		self.root.submit = tkinter.Button(self.root, command=self.button, text="Generate Report", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.root.quit = tkinter.Button(self.root, command=self.quit, text="Close", background=button_bg,
									foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)

		self.root.quit.place(relx=3/5, rely=9/10, anchor="w")

		self.root.mainloop()

	def change_drop2(self, report):

		if report == "List of Books" or report == "List of Visits":
			self.root.loc.place(relx=2 / 5, rely=4 / 10, anchor="e")
			self.root.loc_drop.place(relx=2 / 5, rely=4 / 10, anchor="w")
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
		print("Generated!")
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
		main()

	def quit(self):
		self.root.destroy()

class AllocStats:

	def __init__(self):
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		self.lookup, self.lookup2, schools = sql.get_schools()

		schools.pop(schools.index("Base"))

		popup = tkinter.Tk()
		popup.geometry("300x100")
		popup.config(background=bg)
		progress = 0
		progress_var = tkinter.DoubleVar()
		progress_bar = ttk.Progressbar(popup, variable=progress_var, maximum=len(schools)-1)
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
			time.sleep(0.01)
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

		for i in range(len(sch)):
			print(sch[i], totals[i], alloc[i], over[i])




class BookList:

	def __init__(self, isbns, school):

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
		self.BookList.geometry("400x600")
		self.BookList.title(school)
		self.BookList.config(background=bg)

		self.BookList.table = ttk.Treeview(self.BookList, columns=("title", "quant"))
		self.BookList.table.tag_configure('colour', background=box_bg, foreground=box_txt)
		self.BookList.table.heading("#0", text="ISBN")
		self.BookList.table.heading("#1", text="Title")
		self.BookList.table.heading("#2", text="Quantity")
		self.BookList.table.column("#0", width=85, anchor="w")
		self.BookList.table.column("#1", width=265)
		self.BookList.table.column("#2", width=50)

		for i in range(0, len(titles)):
			self.BookList.table.insert("", index="end", text=isbns2[i], values=(titles[i], quantity[i],), tags=('colour',))

		self.BookList.table.place(x=0, y=0, anchor="nw")

		self.BookList.mainloop()

def main():
	app = Generator()


if __name__ == "__main__":
	main()
