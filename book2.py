import tkinter
import sys
# import img
import urllib
import PIL.Image as Pict
from PIL import ImageTk
import img2gif
import sql
import books_api as books
import json
import homepage


def get_theme():

	with open("D:/Project-Bookworm/settings.json", "r") as file:
		settings = json.load(file)

	with open("D:/Project-Bookworm/theme.json", "r") as readfile:
		theme1 = json.load(readfile)

	theme = settings["theme"]
	db = settings["database_location"]

	bg = theme1[theme]["windows"]["background"]
	text = theme1[theme]["windows"]["text"]
	button_bg = theme1[theme]["button"]["background"]
	butt_txt = theme1[theme]["button"]["text"]
	box_bg = theme1[theme]["textbox"]["background"]
	box_txt = theme1[theme]["textbox"]["foreground"]
	cursor = theme1[theme]["textbox"]["insertbackground"]
	select = theme1[theme]["textbox"]["selectbackground"]
	clickedbg = theme1[theme]["button"]["clickedbg"]
	darkbg = theme1[theme]["windows"]["darkbackground"]

	return bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, darkbg, db


class Book:

	def __init__(self, title=str("None"), author=str("None"), genre=str("None"), released=str("None"),
					binding=str("None"), age=str("None"), label=str("None"), blurb=str("None"),
					img_url=None, isbn=None):

		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, darkbg, db = get_theme()

		self.isbn = isbn
		self.img_url = img_url

		self.root = tkinter.Tk()
		self.root.resizable(False, False)
		self.root.geometry("483x467+574+186")
		self.root.title(title)
		self.root.configure(background=bg)

		self.Canvas1 = tkinter.Canvas(self.root)
		self.Canvas1.place(relx=0.58, rely=0.13, relheight=0.52, relwidth=0.38)
		self.Canvas1.configure(background=darkbg, borderwidth="2", highlightbackground=darkbg, highlightcolor="black",
								insertbackground="black", relief=tkinter.RIDGE, selectbackground="#c4c4c4",
								selectforeground="black", width=183)

		self.titleVar = tkinter.Text(self.root)
		self.titleVar.place(relx=0.17, rely=0.06, relheight=0.05, relwidth=0.77)
		self.titleVar.configure(background=box_bg, foreground=box_txt, insertbackground=cursor, selectbackground=select,
								font="TkTextFont", undo="1", width=374, wrap=tkinter.WORD)

		self.genreVar = tkinter.Text(self.root)
		self.genreVar.place(relx=0.17, rely=0.24, relheight=0.05, relwidth=0.36)
		self.genreVar.configure(background=box_bg, foreground=box_txt, insertbackground=cursor, selectbackground=select,
								font="TkTextFont", undo="1", width=374, wrap=tkinter.WORD)

		self.bindingVar = tkinter.Text(self.root)
		self.bindingVar.place(relx=0.17, rely=0.41, relheight=0.05, relwidth=0.36)
		self.bindingVar.configure(background=box_bg, foreground=box_txt, insertbackground=cursor,
									selectbackground=select, font="TkTextFont", undo="1", width=374, wrap=tkinter.WORD)

		self.ageVar = tkinter.Text(self.root)
		self.ageVar.place(relx=0.17, rely=0.49, relheight=0.05, relwidth=0.36)
		self.ageVar.configure(background=box_bg, foreground=box_txt, insertbackground=cursor, selectbackground=select,
								font="TkTextFont", undo="1", width=374, wrap=tkinter.WORD)

		self.Text7 = tkinter.Text(self.root)
		self.Text7.place(relx=0.17, rely=0.58, relheight=0.05, relwidth=0.36)
		self.Text7.configure(background=box_bg, foreground=box_txt, insertbackground=cursor, selectbackground=select,
								font="TkTextFont", undo="1", width=374, wrap=tkinter.WORD)

		self.blurbVar = tkinter.Text(self.root)
		self.blurbVar.place(relx=0.17, rely=0.69, relheight=0.22, relwidth=0.75)
		self.blurbVar.configure(background=box_bg, foreground=box_txt, insertbackground=cursor, selectbackground=select,
								font="TkTextFont", undo="1", width=374, wrap=tkinter.WORD)

		self.title = tkinter.Label(self.root)
		self.title.place(relx=0.06, rely=0.06, height=21, width=35)
		self.title.configure(activebackground=bg, activeforeground=text, background=bg, foreground=text,
								highlightbackground=bg, text='''Title:''')

		self.Label2 = tkinter.Label(self.root)
		self.Label2.place(relx=0.04, rely=0.15, height=21, width=52)
		self.Label2.configure(activebackground=bg, activeforeground=text, background=bg, foreground=text,
								highlightbackground=bg)
		self.Label2.configure(text='''Author:''')

		self.Label3 = tkinter.Label(self.root)
		self.Label3.place(relx=0.06, rely=0.24, height=21, width=50)
		self.Label3.configure(activebackground=bg, activeforeground=text, background=bg, foreground=text,
								highlightbackground=bg)
		self.Label3.configure(text='''Genre:''')

		self.Label4 = tkinter.Label(self.root)
		self.Label4.place(relx=0.0, rely=0.32, height=21, width=85)
		self.Label4.configure(activebackground=bg, activeforeground=text, background=bg, foreground=text,
								highlightbackground=bg)
		self.Label4.configure(text='''Released:''')

		self.Label5 = tkinter.Label(self.root)
		self.Label5.place(relx=0.02, rely=0.41, height=21, width=53)
		self.Label5.configure(activebackground=bg, activeforeground=text, background=bg, foreground=text,
								highlightbackground=bg)
		self.Label5.configure(text='''Binding:''')

		self.Label6 = tkinter.Label(self.root)
		self.Label6.place(relx=0.06, rely=0.49, height=21, width=36)
		self.Label6.configure(activebackground=bg, activeforeground=text, background=bg, foreground=text,
								highlightbackground=bg)
		self.Label6.configure(text='''Age:''')

		self.Label7 = tkinter.Label(self.root)
		self.Label7.place(relx=0.06, rely=0.58, height=21, width=37)
		self.Label7.configure(activebackground=bg, activeforeground=text, background=bg, foreground=text,
								highlightbackground=bg)
		self.Label7.configure(text='''Label:''')

		self.Label8 = tkinter.Label(self.root)
		self.Label8.place(relx=0.06, rely=0.69, height=21, width=37)
		self.Label8.configure(activebackground=bg, activeforeground=text, background=bg, foreground=text,
								highlightbackground=bg)
		self.Label8.configure(text='''Blurb:''')

		self.releasedVar = tkinter.Text(self.root)
		self.releasedVar.place(relx=0.17, rely=0.32, relheight=0.05, relwidth=0.36)
		self.releasedVar.configure(background=box_bg, foreground=box_txt, insertbackground=cursor,
									selectbackground=select, font="TkTextFont", undo="1", width=374, wrap=tkinter.WORD)

		self.authorVar = tkinter.Text(self.root)
		self.authorVar.place(relx=0.17, rely=0.15, relheight=0.05, relwidth=0.36)
		self.authorVar.configure(background=box_bg, foreground=box_txt, insertbackground=cursor,
									selectbackground=select, font="TkTextFont", undo="1", width=374, wrap=tkinter.WORD)

		self.edit_button = tkinter.Button(command=self.save)
		self.edit_button.place(relx=0.17, rely=0.93, height=24, width=87)
		self.edit_button.configure(text="Save Changes:", background=button_bg, foreground=butt_txt,
									activebackground=clickedbg, activeforeground=butt_txt)

		self.delete_button = tkinter.Button(command=self.delete)
		self.delete_button.place(relx=0.58, rely=0.93, height=24, width=120)
		self.delete_button.configure(text="Revert to online data:", background=button_bg, foreground=butt_txt,
										activebackground=clickedbg, activeforeground=butt_txt)

		self.close_button = tkinter.Button(command=self.close)
		self.close_button.place(relx=0.365, rely=0.93, height=24, width=100)
		self.close_button.configure(text="Close", background=button_bg, foreground=butt_txt,
									activebackground=clickedbg, activeforeground=butt_txt)

		'''
		if title == None:
			title = str("None")

		if author == None:
			author = str("None")

		if genre == None:
			genre = str("None")

		if released == None:
			released = str("None")
		'''

		if binding is None:
			binding = str("None")
		'''
		if age == None:
			age = str("None")
		'''
		if label is None:
			label = str("None")
		'''
		if blurb == None:
			blurb = str("None")
		'''

		self.titleVar.insert(tkinter.INSERT, title)
		self.authorVar.insert(tkinter.INSERT, author)
		self.genreVar.insert(tkinter.INSERT, genre)
		self.releasedVar.insert(tkinter.INSERT, released)
		self.bindingVar.insert(tkinter.INSERT, binding)
		self.ageVar.insert(tkinter.INSERT, age)

		self.Text7.insert(tkinter.INSERT, label)
		self.blurbVar.insert(tkinter.INSERT, blurb)

		try:
			urllib.request.urlretrieve(img_url, "D:/Project-Bookworm/image.jpg")
			img2gif.main()
			img2gif.resize()
			self.photo = ImageTk.PhotoImage(file="D:/Project-Bookworm/image.gif")
		except TypeError:
			img2gif.error()
			img2gif.resizeError()
			self.photo = ImageTk.PhotoImage(file="D:/Project-Bookworm/error.gif")
		except ValueError:
			img2gif.error()
			img2gif.resizeError()
			self.photo = ImageTk.PhotoImage(file="D:/Project-Bookworm/error.gif")

		self.Canvas1.create_image(0, 123, image=self.photo, anchor='w')

		self.root.mainloop()

	def get_changes(self):
		a = str(self.titleVar.get("0.0", tkinter.END))
		b = str(self.authorVar.get("0.0", tkinter.END))
		c = str(self.genreVar.get("0.0", tkinter.END))
		d = str(self.releasedVar.get("0.0", tkinter.END))
		e = str(self.bindingVar.get("0.0", tkinter.END))
		f = str(self.ageVar.get("0.0", tkinter.END))
		g = str(self.Text7.get("0.0", tkinter.END))
		h = str(self.blurbVar.get("0.0", tkinter.END))
		# i = self.img_url
		return a, b, c, d, e, f, g, h  # , i

	def close(self):
		self.root.destroy()
		#homepage.homepage()

	def save(self):
		a, b, c, d, e, f, g, h = self.get_changes()
		print(a, b, c, d, e, f, g, h)
		# i = "None"
		sql.add_book(self.isbn, a, b, c, d, e, f, g, h, self.isbn)
		self.close()

	def delete(self):
		self.close()

	def img_change(self):
		self.img_url = input("image url?")
