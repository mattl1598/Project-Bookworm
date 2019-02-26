import tkinter
import locations
import json
import datetime
import sql

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


class CalendarMain:

	def __init__(self):
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()
		self.root = tkinter.Tk()
		self.root.title("Calendar")
		self.root.geometry("1280x720")
		self.root.resizable(False, False)
		self.root.configure(background=bg)

		self.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
					"November", "December"]
		self.month = tkinter.StringVar(self.root)

		years = []
		self.year = tkinter.StringVar(self.root)
		now = datetime.datetime.now()

		for i in range(2018, int(now.year)+10):
			years.append(i)

		self.month.set(self.months[now.month - 1])
		self.year.set(now.year)

		self.root.month_drop = tkinter.OptionMenu(self.root, self.month, *self.months, command=self.update_calendar)
		self.root.month_drop.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
										activeforeground=butt_txt, highlightthickness=0, highlightcolor=bg,
										highlightbackground=bg)
		self.root.month_drop["menu"].config(bg=button_bg, foreground=butt_txt, bd="0", activebackground="SystemHighlight",
											activeforeground=butt_txt)

		self.root.year_drop = tkinter.OptionMenu(self.root, self.year, *years, command=self.update_calendar)
		self.root.year_drop.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
										activeforeground=butt_txt, highlightthickness=0, highlightcolor=bg,
										highlightbackground=bg)
		self.root.year_drop["menu"].config(bg=button_bg, foreground=butt_txt, bd="0",
											activebackground="SystemHighlight",
											activeforeground=butt_txt)

		self.root.month_drop.place(relx=885/1280, rely=10/720, relwidth=150/1280, relheight=25/720, anchor="nw")
		self.root.year_drop.place(relx=1045/1280, rely=10/720, relwidth=155/1280, relheight=25/720, anchor="nw")

		self.root.days = tkinter.Canvas(self.root, bg=box_bg)
		self.root.days.place(relx=80/1280, rely=45/720, relwidth=1120/1280, relheight=22/720)

		self.root.calendar = tkinter.Canvas(self.root)
		self.root.calendar.config(bg=box_bg)
		self.root.calendar.place(relx=80/1280, rely=65/720, relwidth=1120/1280, relheight=630/720)

		# self.button = tkinter.Button(self.root, text="test", command=self.event_test).place(x=0, y=0)

		days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

		for i in range(1, 8):
			x = i*160
			y1 = 0
			y2 = 630
			self.root.calendar.create_line(x, y1, x, y2, fill=box_txt, tags="tag")
			self.root.days.i = tkinter.Label(self.root.days, text=days[i-1], bg=box_bg, fg=box_txt).place(x=(i*160)-80, y=10, anchor="center")
			self.root.days.create_line(x, y1, x, y2, fill=box_txt, width=3, tags="tag")

		self.root.days.line = tkinter.Canvas(self.root.days, bg=box_bg).place(x=0, y=0, width=1120, height=2)

		for i in range(1,6):
			x1 = 0
			x2 = 1120
			y = i*105
			self.root.calendar.create_line(x1, y, x2, y, fill=box_txt, tags="tag")

		days_array = self.days_array()

		self.labels = []
		self.label_vars = []
		self.list_boxes = []

		for y in range(0, 6):
			for x in range(0, 7):
				i = x + (y * 7)

				self.label_vars.append(tkinter.StringVar())
				self.label_vars[i].set(days_array[y][x])

				self.root.calendar.i = tkinter.Label(self.root.calendar, textvariable=self.label_vars[i], bg=box_bg, fg=box_txt)
				self.labels.append(self.root.calendar.i)

				self.list_boxes.append(tkinter.Listbox(self.root.calendar, bg=box_bg, fg=box_txt, bd=0, highlightthickness=0))
				self.list_boxes[i].bind('<Double-Button>', self.event)

		for label in self.labels:
			x = self.labels.index(label) % 7
			y = self.labels.index(label) // 7
			label.place(x=(x*160)+2, y=(y*105)+2)

		for list in self.list_boxes:
			x = self.list_boxes.index(list) % 7
			y = self.list_boxes.index(list) // 7
			list.place(x=(x*160)+2, y=(y*105)+20, width=156, height=81)

		# self.root.bind("<Configure>", self.update_canvas)

		self.update_events()

		self.root.mainloop()

	def update_calendar(self, test):
		self.update_days()
		self.update_events()

	def update_events(self):
		for list in self.list_boxes:
			list.delete(0, 'end')

		start = self.month_start()
		all_events = sql.get_all_events()
		month = self.months.index(self.month.get())+1
		year = int(self.year.get())

		# self.lookup = [[],[]]

		events = []
		for i in range(len(all_events)):
			if all_events[i][2]["year"] == year and all_events[i][2]["month"] == month:
				events.append(all_events[i])

		for i in range(len(events)):
			note = events[i][5] + " - " + sql.get_school_name(events[i][1]) + " - " + str(events[i][0])
			self.list_boxes[int(events[i][2]["day"])+start-1].insert('end', note)

	def update_days(self):
		days_array = self.days_array()
		for y in range(0, 6):
			for x in range(0, 7):
				i = x+(y*7)
				self.label_vars[i].set(days_array[y][x])
		self.root.update()

	def update_canvas(self, test):
		xscale = self.root.calendar.winfo_width() / 1120
		yscale = self.root.calendar.winfo_height() / 630
		self.root.calendar.scale("tag", 0, 0, xscale, yscale)

	def month_start(self):
		ans = datetime.date(int(self.year.get()), self.months.index(self.month.get())+1, 1)
		# day = ans.strftime("%A")
		num = ans.weekday()
		return num

	def is_leap_year(self):
		if int(self.year.get()) % 4 == 0:
			if int(self.year.get()) % 100 != 0:
				flag = True
			elif int(self.year.get()) % 400 == 0:
				flag = True
			else:
				flag = False
		else:
			flag = False

	def days_array(self):
		num = self.month_start()
		days = []
		if self.is_leap_year():
			month_lengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		else:
			month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		for i in range(0, num):
			days.append("")
		for i in range(0, month_lengths[self.months.index(self.month.get())]):
			days.append(i+1)
		for i in range(0, 42-len(days)):
			days.append("")

		week1 = []
		week2 = []
		week3 = []
		week4 = []
		week5 = []
		week6 = []
		for i in range(0, 7):
			week1.append(days.pop(0))
		for i in range(0, 7):
			week2.append(days.pop(0))
		for i in range(0, 7):
			week3.append(days.pop(0))
		for i in range(0, 7):
			week4.append(days.pop(0))
		for i in range(0, 7):
			week5.append(days.pop(0))
		for i in range(0, 7):
			week6.append(days.pop(0))

		return [week1, week2, week3, week4, week5, week6]

	def event_test(self):
		self.root.destroy()
		app = EventViewer()

	def event(self, test):
		raw = str(self.root.calendar.focus_get())
		listbox = raw[raw.index(".!listbox")+9:]
		note = self.list_boxes[int(listbox)-1].get(self.list_boxes[int(listbox)-1].curselection())
		self.root.destroy()
		data = note.split(" - ")
		app = EventViewer(int(data[2]))


class EventViewer:
	def __init__(self, event_id):

		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		self.root = tkinter.Tk()
		self.root.geometry("400x400")
		self.root.config(bg=bg)

		self.event_id = event_id

		self.event = sql.get_event(self.event_id)[0]

		values = []
		for j in range(len(self.event[2].values())):
			values.append(str(list(self.event[2].values())[j]).zfill(2))

		self.event[2] = "-".join(values)

		self.school = tkinter.StringVar(self.root)

		self.lookup, self.lookup2, schools = sql.get_schools()

		"""
		self.vars = []
		for i in range(0, 6):
			if i != 2:
				self.vars.append(tkinter.StringVar().set(self.event[i]))
			else:
				values = []
				for j in range(len(self.event[i].values())):
					values.append(str(list(self.event[i].values())[j]))
				self.vars.append(tkinter.StringVar(self.root).set("-".join(values)))
		"""
		self.root.schoolL = tkinter.Label(self.root, text="School:", bg=bg, fg=box_txt)
		self.root.schoolE = tkinter.OptionMenu(self.root, self.school, *schools)
		self.root.schoolE.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
									activeforeground=butt_txt, highlightthickness=0, highlightcolor=bg,
									highlightbackground=bg)
		self.root.schoolE["menu"].config(bg=button_bg, foreground=butt_txt, bd="0", activebackground="SystemHighlight",
											activeforeground=butt_txt)

		self.root.dateL = tkinter.Label(self.root, text="Date:", bg=bg, fg=box_txt)
		self.root.dateE = tkinter.Entry(self.root, bg=box_bg, fg=box_txt, insertbackground=cursor,
										selectbackground=select)

		self.root.timeL = tkinter.Label(self.root, text="Time:", bg=bg, fg=box_txt)
		self.root.timeE = tkinter.Entry(self.root, bg=box_bg, fg=box_txt, insertbackground=cursor,
										selectbackground=select)

		self.root.typeL = tkinter.Label(self.root, text="Type:", bg=bg, fg=box_txt)
		self.root.typeE = tkinter.Entry(self.root, bg=box_bg, fg=box_txt, insertbackground=cursor,
										selectbackground=select)

		self.root.notesL = tkinter.Label(self.root, text="Notes:", bg=bg, fg=box_txt)
		self.root.notesE = tkinter.Text(self.root, bg=box_bg, fg=box_txt, insertbackground=cursor,
										selectbackground=select)

		self.labels = [self.root.schoolL, self.root.dateL, self.root.timeL, self.root.typeL, self.root.notesL]
		self.entry = [self.root.schoolE, self.root.dateE, self.root.timeE, self.root.typeE, self.root.notesE]

		for label in self.labels:
			label.place(x=70, y=(self.labels.index(label)*50)+30, anchor="e")

		for entry in self.entry:
			entry.place(x=75, y=(self.entry.index(entry)*50)+30, height=30, width=275, anchor="w")

		self.root.notesE.place(x=75, y=215, height=125, width=275, anchor="nw")

		self.populate()

		# self.button = tkinter.Button(self.root, text="test", command=self.update_event).place(x=0, y=0)

		self.root.mainloop()

	def populate(self):
		index = [2, 5, 3, 4]
		widgets = self.entry
		widgets.pop(0)
		self.school.set(sql.get_school_name(self.event[1]))
		for entry in widgets:
			value = index[widgets.index(entry)]
			temp = str(self.event[value])
			if entry != widgets[3]:
				entry.insert(0, temp)
			else:
				if str(self.event[4]) != "None":
					entry.insert(tkinter.END, str(self.event[4]))
				else:
					entry.insert(tkinter.END, "")

	def update_event(self):
		event = []
		for entry in self.entry:
			try:
				event.append(entry.get())
			except TypeError:
				event.append(entry.get('1.0', tkinter.END).rstrip("\n\r"))
		print(event)


def main():
	CalendarMain()


if __name__ == "__main__":
	main()
