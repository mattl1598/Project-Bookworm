import homepage
import tkinter
import json
import webbrowser
import urllib
import sql
import homepage


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


class Deets:

	def __init__(self, school_id, mode, lookup=None):

		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		self.root = tkinter.Tk()

		size = str(int((self.root.winfo_screenwidth()*(55/192))))
		x = "x"
		size += x
		size += str(int(self.root.winfo_screenheight()*(35/54)))

		self.root.geometry(size)
		self.root.title("Test")
		self.root.config(bg=bg)

		self.root.sch = tkinter.Label(self.root)

		self.root.schL = tkinter.Label(self.root, foreground=text, bg=bg, text="School Name:")
		self.root.schE = tkinter.Text(self.root)
		self.root.schL.place(relx=(2/11), rely=(2/35), anchor="ne")

		self.root.HT = tkinter.Text(self.root)
		self.root.HTL = tkinter.Label(self.root)
		self.root.HTL.config(text="Head Teacher: ", foreground=text, bg=bg)

		self.root.HT.place(relx=(2/11), rely=0.1, width=250, height=22, anchor="nw")
		self.root.HTL.place(relx=(2/11), rely=0.1, anchor="ne")

		self.root.LastEx = tkinter.Text(self.root)
		self.root.LastExL = tkinter.Label(self.root)

		self.root.LastExL.config(text="Last Exchange: ", foreground=text, bg=bg)
		self.root.LastEx.place(relx=(2/11), rely=(1/7), width=250, height=22, anchor="nw")
		self.root.LastExL.place(relx=(2/11), rely=(1/7), anchor="ne")

		self.root.contact = tkinter.Text(self.root)
		self.root.contactL = tkinter.Label(self.root)

		self.root.contactL.config(text="Contact: ", foreground=text, bg=bg)
		self.root.contact.place(relx=(2/11), rely=(13/70), width=250, height=22, anchor="nw")
		self.root.contactL.place(relx=(2/11), rely=(13/70), anchor="ne")

		self.root.dfe = tkinter.Text(self.root)
		self.root.dfeL = tkinter.Label(self.root)

		self.root.dfeL.config(text="DFE No': ", foreground=text, bg=bg)
		self.root.dfe.place(relx=(2/11), rely=(16/70), width=250, height=22, anchor="nw")
		self.root.dfeL.place(relx=(2/11), rely=(16/70), anchor="ne")

		self.root.Add = tkinter.Text(self.root)
		self.root.AddL = tkinter.Label(self.root)
		self.root.AddButt = tkinter.Button(self.root, command=self.directions)

		self.root.AddL.config(text="Address: ", foreground=text, bg=bg)
		self.root.AddButt.config(text="Directions: ", foreground=butt_txt, bg=button_bg, activebackground=clickedbg,
										activeforeground=butt_txt)
		self.root.Add.place(relx=(2/11), y=190, width=250, height=82, anchor="nw")
		self.root.AddL.place(relx=(2/11), y=190, anchor="ne")
		self.root.AddButt.place(relx=0.654545, y=190)

		self.root.data = tkinter.Button(self.root, foreground=butt_txt, bg=button_bg, activebackground=clickedbg,
										activeforeground=butt_txt)

		if mode == "edit" or mode == "new":
			if mode == "edit":

				self.school_id = school_id
				self.lookup = lookup
				self.data = sql.get_school_deets(self.school_id)

				self.root.data.config(command=self.edit, text="Save Changes")
				self.root.sch.config(text=self.data["name"], foreground=text, bg=bg, font=("TkDefault", 30))
				self.root.schE.insert(tkinter.INSERT, self.data["name"])
				self.root.HT.insert(tkinter.INSERT, self.data["HT"])
				self.root.LastEx.insert(tkinter.INSERT, self.data["lastEx"])
				self.root.contact.insert(tkinter.INSERT, self.data["Contact"])
				self.root.dfe.insert(tkinter.INSERT, self.data["DFE"])
				self.root.Add.insert(tkinter.INSERT, self.data["address"])
			else:
				self.root.data.config(command=self.new, text="Add New School")

			self.root.data.place(x=445, y=650, height=30, anchor="ne")

			for t in (self.root.schE, self.root.HT, self.root.LastEx, self.root.contact, self.root.dfe, self.root.Add,
						self.root.data):
				t.bind('<Tab>', lambda e, t=t: focus_next(t))
				t.bind('<Shift-Tab>', lambda e, t=t: focus_prev(t))

			self.root.schE.place(relx=(2/11), rely=(2/35), relwidth=(250/550), relheight=(22/700), anchor="nw")

		else:
			print("REEEEEEEEEEEEEEEE")
			self.school_id = school_id
			self.lookup = lookup
			self.data = sql.get_school_deets(self.school_id)
			print("aaaaaa")
			print(self.data)
			self.root.sch.config(text=self.data["name"], foreground=text, bg=bg, font=("TkDefault", 30))
			self.root.sch.place(relx=(2 / 11), rely=(1 / 70))
			self.root.HT.insert(tkinter.INSERT, self.data["HT"])
			self.root.LastEx.insert(tkinter.INSERT, self.data["lastEx"])
			self.root.contact.insert(tkinter.INSERT, self.data["Contact"])
			self.root.dfe.insert(tkinter.INSERT, self.data["DFE"])
			self.root.Add.insert(tkinter.INSERT, self.data["address"])

		self.root.quit = tkinter.Button(self.root, text="Quit", command=self.quit, foreground=butt_txt, bg=button_bg,
										activebackground=clickedbg, activeforeground=butt_txt)
		self.root.quit.place(x=455, y=650, width=45, height=30)

		self.root.mainloop()

	def quit(self):
		self.root.destroy()
		homepage.main()

	def edit(self):
		print("REEEEEEEEEEEEEEEEEE")

	def new(self):
		data = [self.root.schE.get("0.0", 'end-1c'), self.root.HT.get("0.0", 'end-1c'),
					self.root.LastEx.get("0.0", 'end-1c'), self.root.contact.get("0.0", 'end-1c'),
					self.root.dfe.get("0.0", 'end-1c'), self.root.Add.get("0.0", 'end-1c')]
		print(sql.new_school(data))

	def directions(self):
		add = self.root.Add.get("0.0", tkinter.END)
		url = "https://www.google.com/maps/search/?api=1&query="
		urladd = urllib.parse.quote_plus(add)
		url += urladd
		webbrowser.open_new(url)






class entry:

	def __init__(self):
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		self.root = tkinter.Tk()

		size = str(int((self.root.winfo_screenwidth()*(40/192))))
		x = "x"
		size += x
		size += str(int(self.root.winfo_screenheight()*(10/54)))

		self.root.geometry(size)
		self.root.config(bg=bg)

		self.root.buttonNew = tkinter.Button(command=self.new, text="New School", foreground=butt_txt, bg=button_bg,
												activebackground=clickedbg, activeforeground=butt_txt)
		self.root.buttonNew.place(relx=0.1, rely=0.05, relheight=0.2, relwidth=0.2)

		self.root.buttonView = tkinter.Button(command=lambda: self.view("view"), text="View School",
												foreground=butt_txt, bg=button_bg,
												activebackground=clickedbg, activeforeground=butt_txt)
		self.root.buttonView.place(relx=0.1, rely=0.25, relheight=0.2, relwidth=0.2)

		self.root.buttonEdit = tkinter.Button(command=lambda: self.view("edit"), text="Edit School",
												foreground=butt_txt, bg=button_bg,
												activebackground=clickedbg, activeforeground=butt_txt)
		self.root.buttonEdit.place(relx=0.1, rely=0.45, relheight=0.2, relwidth=0.2)

		self.school = tkinter.StringVar(self.root)

		self.lookup, self.lookup2, schools = sql.get_schools()

		self.root.schools = tkinter.OptionMenu(self.root, self.school, *schools)
		self.root.schools.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
									activeforeground=butt_txt, highlightthickness=0, highlightcolor=bg,
									highlightbackground=bg)
		self.root.schools["menu"].config(bg=button_bg, foreground=butt_txt, bd="0", activebackground="SystemHighlight",
											activeforeground=butt_txt)
		self.root.schools.place(relx=0.5, rely=0.25, relheight=0.25, relwidth=0.4)

		self.root.mainloop()

	def new(self):
		print("YEEEEEET")
		self.root.destroy()
		init("YEEEEEEEEET", "new", None)

	def view(self, mode):
		school_name = self.school.get()
		school_id = self.lookup[school_name]
		print(self.lookup)
		self.root.destroy()
		init(school_id, mode, self.lookup2)


def start():
	app = entry()


def init(school_id, mode, lookup):
	app = Deets(school_id, mode, lookup)


def focus_next(widget):
	widget.tk_focusNext().focus_set()
	return 'break'


def focus_prev(widget):
	widget.tk_focusPrev().focus_set()
	return 'break'
