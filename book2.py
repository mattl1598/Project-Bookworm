import tkinter
import sys
import img
import urllib
import PIL.Image as pict
from PIL import ImageTk
import img2gif
import sql

class Book:
	def __init__(self, title=str("None"), author = str("None"), genre=str("None"), released=str("None"), binding= str("None"), age=str("None"), label=str("None"), blurb=str("None"), imgURL=str(img.imgGet()), isbn = None):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''

		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#d9d9d9' # X11 color: 'gray85'

		self.isbn = isbn
		self.imgURL = imgURL

		self.root = tkinter.Tk()
		self.root.resizable(False, False)
		self.root.geometry("483x467+574+186")
		self.root.title(title)
		self.root.configure(background="#d9d9d9")
		self.root.configure(highlightbackground="#d9d9d9")
		self.root.configure(highlightcolor="black")



		self.Canvas1 = tkinter.Canvas(self.root)
		self.Canvas1.place(relx=0.58, rely=0.13, relheight=0.52, relwidth=0.38)
		self.Canvas1.configure(background="#d9d9d9")
		self.Canvas1.configure(borderwidth="2")
		self.Canvas1.configure(highlightbackground="#d9d9d9")
		self.Canvas1.configure(highlightcolor="black")
		self.Canvas1.configure(insertbackground="black")
		self.Canvas1.configure(relief=tkinter.RIDGE)
		self.Canvas1.configure(selectbackground="#c4c4c4")
		self.Canvas1.configure(selectforeground="black")
		self.Canvas1.configure(width=183)


		self.titleVar = tkinter.Text(self.root)
		self.titleVar.place(relx=0.17, rely=0.06, relheight=0.05, relwidth=0.77)
		self.titleVar.configure(background="white")
		self.titleVar.configure(font="TkTextFont")
		self.titleVar.configure(foreground="black")
		self.titleVar.configure(highlightbackground="#d9d9d9")
		self.titleVar.configure(highlightcolor="black")
		self.titleVar.configure(insertbackground="black")
		self.titleVar.configure(selectbackground="#c4c4c4")
		self.titleVar.configure(selectforeground="black")
		self.titleVar.configure(undo="1")
		self.titleVar.configure(width=374)
		self.titleVar.configure(wrap=tkinter.WORD)

		self.genreVar = tkinter.Text(self.root)
		self.genreVar.place(relx=0.17, rely=0.24, relheight=0.05, relwidth=0.36)
		self.genreVar.configure(background="white")
		self.genreVar.configure(font="TkTextFont")
		self.genreVar.configure(foreground="black")
		self.genreVar.configure(highlightbackground="#d9d9d9")
		self.genreVar.configure(highlightcolor="black")
		self.genreVar.configure(insertbackground="black")
		self.genreVar.configure(selectbackground="#c4c4c4")
		self.genreVar.configure(selectforeground="black")
		self.genreVar.configure(undo="1")
		self.genreVar.configure(width=174)
		self.genreVar.configure(wrap=tkinter.WORD)

		self.bindingVar = tkinter.Text(self.root)
		self.bindingVar.place(relx=0.17, rely=0.41, relheight=0.05
				, relwidth=0.36)
		self.bindingVar.configure(background="white")
		self.bindingVar.configure(font="TkTextFont")
		self.bindingVar.configure(foreground="black")
		self.bindingVar.configure(highlightbackground="#d9d9d9")
		self.bindingVar.configure(highlightcolor="black")
		self.bindingVar.configure(insertbackground="black")
		self.bindingVar.configure(selectbackground="#c4c4c4")
		self.bindingVar.configure(selectforeground="black")
		self.bindingVar.configure(undo="1")
		self.bindingVar.configure(width=174)
		self.bindingVar.configure(wrap=tkinter.WORD)

		self.ageVar = tkinter.Text(self.root)
		self.ageVar.place(relx=0.17, rely=0.49, relheight=0.05, relwidth=0.36)
		self.ageVar.configure(background="white")
		self.ageVar.configure(font="TkTextFont")
		self.ageVar.configure(foreground="black")
		self.ageVar.configure(highlightbackground="#d9d9d9")
		self.ageVar.configure(highlightcolor="black")
		self.ageVar.configure(insertbackground="black")
		self.ageVar.configure(selectbackground="#c4c4c4")
		self.ageVar.configure(selectforeground="black")
		self.ageVar.configure(undo="1")
		self.ageVar.configure(width=174)
		self.ageVar.configure(wrap=tkinter.WORD)

		self.Text7 = tkinter.Text(self.root)
		self.Text7.place(relx=0.17, rely=0.58, relheight=0.05, relwidth=0.36)
		self.Text7.configure(background="white")
		self.Text7.configure(font="TkTextFont")
		self.Text7.configure(foreground="black")
		self.Text7.configure(highlightbackground="#d9d9d9")
		self.Text7.configure(highlightcolor="black")
		self.Text7.configure(insertbackground="black")
		self.Text7.configure(selectbackground="#c4c4c4")
		self.Text7.configure(selectforeground="black")
		self.Text7.configure(undo="1")
		self.Text7.configure(width=174)
		self.Text7.configure(wrap=tkinter.WORD)

		self.blurbVar = tkinter.Text(self.root)
		self.blurbVar.place(relx=0.17, rely=0.69, relheight=0.22, relwidth=0.75)
		self.blurbVar.configure(background="white")
		self.blurbVar.configure(font="TkTextFont")
		self.blurbVar.configure(foreground="black")
		self.blurbVar.configure(highlightbackground="#d9d9d9")
		self.blurbVar.configure(highlightcolor="black")
		self.blurbVar.configure(insertbackground="black")
		self.blurbVar.configure(selectbackground="#c4c4c4")
		self.blurbVar.configure(selectforeground="black")
		self.blurbVar.configure(undo="1")
		self.blurbVar.configure(width=364)
		self.blurbVar.configure(wrap=tkinter.WORD)

		self.title = tkinter.Label(self.root)
		self.title.place(relx=0.06, rely=0.06, height=21, width=35)
		self.title.configure(activebackground="#f9f9f9")
		self.title.configure(activeforeground="black")
		self.title.configure(background="#d9d9d9")
		self.title.configure(disabledforeground="#a3a3a3")
		self.title.configure(foreground="#000000")
		self.title.configure(highlightbackground="#d9d9d9")
		self.title.configure(highlightcolor="black")
		self.title.configure(text='''Title:''')

		self.Label2 = tkinter.Label(self.root)
		self.Label2.place(relx=0.04, rely=0.15, height=21, width=52)
		self.Label2.configure(activebackground="#f9f9f9")
		self.Label2.configure(activeforeground="black")
		self.Label2.configure(background="#d9d9d9")
		self.Label2.configure(disabledforeground="#a3a3a3")
		self.Label2.configure(foreground="#000000")
		self.Label2.configure(highlightbackground="#d9d9d9")
		self.Label2.configure(highlightcolor="black")
		self.Label2.configure(text='''Author:''')

		self.Label3 = tkinter.Label(self.root)
		self.Label3.place(relx=0.06, rely=0.24, height=21, width=50)
		self.Label3.configure(activebackground="#f9f9f9")
		self.Label3.configure(activeforeground="black")
		self.Label3.configure(background="#d9d9d9")
		self.Label3.configure(disabledforeground="#a3a3a3")
		self.Label3.configure(foreground="#000000")
		self.Label3.configure(highlightbackground="#d9d9d9")
		self.Label3.configure(highlightcolor="black")
		self.Label3.configure(text='''Genre:''')

		self.Label4 = tkinter.Label(self.root)
		self.Label4.place(relx=0.0, rely=0.32, height=21, width=85)
		self.Label4.configure(activebackground="#f9f9f9")
		self.Label4.configure(activeforeground="black")
		self.Label4.configure(background="#d9d9d9")
		self.Label4.configure(disabledforeground="#a3a3a3")
		self.Label4.configure(foreground="#000000")
		self.Label4.configure(highlightbackground="#d9d9d9")
		self.Label4.configure(highlightcolor="black")
		self.Label4.configure(text='''Released:''')

		self.Label5 = tkinter.Label(self.root)
		self.Label5.place(relx=0.02, rely=0.41, height=21, width=53)
		self.Label5.configure(activebackground="#f9f9f9")
		self.Label5.configure(activeforeground="black")
		self.Label5.configure(background="#d9d9d9")
		self.Label5.configure(disabledforeground="#a3a3a3")
		self.Label5.configure(foreground="#000000")
		self.Label5.configure(highlightbackground="#d9d9d9")
		self.Label5.configure(highlightcolor="black")
		self.Label5.configure(text='''Binding:''')

		self.Label6 = tkinter.Label(self.root)
		self.Label6.place(relx=0.06, rely=0.49, height=21, width=36)
		self.Label6.configure(activebackground="#f9f9f9")
		self.Label6.configure(activeforeground="black")
		self.Label6.configure(background="#d9d9d9")
		self.Label6.configure(disabledforeground="#a3a3a3")
		self.Label6.configure(foreground="#000000")
		self.Label6.configure(highlightbackground="#d9d9d9")
		self.Label6.configure(highlightcolor="black")
		self.Label6.configure(text='''Age:''')

		self.Label7 = tkinter.Label(self.root)
		self.Label7.place(relx=0.06, rely=0.58, height=21, width=37)
		self.Label7.configure(activebackground="#f9f9f9")
		self.Label7.configure(activeforeground="black")
		self.Label7.configure(background="#d9d9d9")
		self.Label7.configure(disabledforeground="#a3a3a3")
		self.Label7.configure(foreground="#000000")
		self.Label7.configure(highlightbackground="#d9d9d9")
		self.Label7.configure(highlightcolor="black")
		self.Label7.configure(text='''Label:''')

		self.Label8 = tkinter.Label(self.root)
		self.Label8.place(relx=0.06, rely=0.69, height=21, width=37)
		self.Label8.configure(activebackground="#f9f9f9")
		self.Label8.configure(activeforeground="black")
		self.Label8.configure(background="#d9d9d9")
		self.Label8.configure(disabledforeground="#a3a3a3")
		self.Label8.configure(foreground="#000000")
		self.Label8.configure(highlightbackground="#d9d9d9")
		self.Label8.configure(highlightcolor="black")
		self.Label8.configure(text='''Blurb:''')

		self.releasedVar = tkinter.Text(self.root)
		self.releasedVar.place(relx=0.17, rely=0.32, relheight=0.05
				, relwidth=0.36)
		self.releasedVar.configure(background="white")
		self.releasedVar.configure(font="TkTextFont")
		self.releasedVar.configure(foreground="black")
		self.releasedVar.configure(highlightbackground="#d9d9d9")
		self.releasedVar.configure(highlightcolor="black")
		self.releasedVar.configure(insertbackground="black")
		self.releasedVar.configure(selectbackground="#c4c4c4")
		self.releasedVar.configure(selectforeground="black")
		self.releasedVar.configure(undo="1")
		self.releasedVar.configure(width=174)
		self.releasedVar.configure(wrap=tkinter.WORD)

		self.authorVar = tkinter.Text(self.root)
		self.authorVar.place(relx=0.17, rely=0.15, relheight=0.05, relwidth=0.36)

		self.authorVar.configure(background="white")
		self.authorVar.configure(font="TkTextFont")
		self.authorVar.configure(foreground="black")
		self.authorVar.configure(highlightbackground="#d9d9d9")
		self.authorVar.configure(highlightcolor="black")
		self.authorVar.configure(insertbackground="black")
		self.authorVar.configure(selectbackground="#c4c4c4")
		self.authorVar.configure(selectforeground="black")
		self.authorVar.configure(undo="1")
		self.authorVar.configure(width=174)
		self.authorVar.configure(wrap=tkinter.WORD)

		self.edit_button = tkinter.Button(command = self.save)
		self.edit_button.place(relx=0.17, rely=0.93, height=24, width=87)
		self.edit_button.configure(text = "Save Changes:")

		self.delete_button = tkinter.Button(command = self.delete)
		self.delete_button.place(relx=0.58, rely=0.93, height=24, width=120)
		self.delete_button.configure(text="Revert to online data:")

		self.close_button = tkinter.Button(command = self.close)
		self.close_button.place(relx=0.365, rely=0.93, height=24, width=100)
		self.close_button.configure(text = "Close")




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
		if binding == None:
			binding = str("None")
		'''
		if age == None:
			age = str("None")
		'''
		if label == None:
			label = str("None")
		'''
		if blurb == None:
			blurb = str("None")
		'''

		self.titleVar.insert(tkinter.INSERT, title)
		self.authorVar.insert(tkinter.INSERT, author)
		self.genreVar.insert(tkinter.INSERT, genre)
		print(released)
		self.releasedVar.insert(tkinter.INSERT, released)
		self.bindingVar.insert(tkinter.INSERT, binding)
		self.ageVar.insert(tkinter.INSERT,age)
		self.Text7.insert(tkinter.INSERT, label)
		self.blurbVar.insert(tkinter.INSERT, blurb)

		if imgURL == img.imgGet():
			img2gif.error()
			img2gif.resizeError()
			self.photo = ImageTk.PhotoImage(file="D:/pyscripter/pycharm/projects/bookworm/error.gif")
		else:
			print(imgURL)
			urllib.request.urlretrieve(imgURL, "D:/pyscripter/pycharm/projects/bookworm/image.jpg")
			img2gif.main()
			img2gif.resize()
			self.photo = ImageTk.PhotoImage(file = "D:/pyscripter/pycharm/projects/bookworm/image.gif")
		self.Canvas1.create_image(0, 123, image = self.photo, anchor = 'w')
		#print(self.Canvas1.cget("width"))
		#print(self.Canvas1.cget("height"))

		self.root.mainloop()

	def getChanges(self):
		a = str(self.titleVar.get("0.0", tkinter.END))
		b = str(self.authorVar.get("0.0", tkinter.END))
		c = str(self.genreVar.get("0.0", tkinter.END))
		d = str(self.releasedVar.get("0.0", tkinter.END))
		e = str(self.bindingVar.get("0.0", tkinter.END))
		f = str(self.ageVar.get("0.0", tkinter.END))
		g = str(self.Text7.get("0.0", tkinter.END))
		h = str(self.blurbVar.get("0.0", tkinter.END))
		#i = self.imgURL
		return a, b, c, d, e, f, g, h#, i

	def close(self):
		self.root.destroy()

	def save(self):
		a, b, c, d, e, f, g, h = self.getChanges()
		print(a, b, c, d, e, f, g, h)
		#i = "None"
		sql.addBook(self.isbn, a, b, c, d, e, f, g, h, self.isbn)
		self.close()

	def delete(self):
		self.close()
