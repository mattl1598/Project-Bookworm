#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#	Jun 08, 2018 10:32:08 PM

import sys
import img
import urllib
import PIL.Image as pict
from PIL import ImageTk

try:
	from Tkinter import *
except ImportError:
	from tkinter import *

try:
	import ttk
	py3 = False
except ImportError:
	import tkinter.ttk as ttk
	py3 = True

import unknown_support

def vp_start_gui(a):
	'''Starting point when module is the main routine.'''
	global val, w, root
	root = Tk()
	top = New_Toplevel (root)
	unknown_support.init(root, top)
	root.mainloop()

w = None
def create_New_Toplevel(root):
	'''Starting point when module is imported by another program.'''
	global w, w_win, rt
	rt = root
	w = Toplevel(root)
	top = New_Toplevel (w)
	unknown_support.init(w, top)
	return (w, top)

def destroy_New_Toplevel():
	global w
	w.destroy()
	w = None


class New_Toplevel:
	def __init__(self, top=None, title=str("None"), author = str("None"), genre=str("None"), released=str("None"), binding= str("None"), age=str("None"), label=str("None"), blurb=str("None"), imgURL=str(img.imgGet())):
		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''

		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#d9d9d9' # X11 color: 'gray85'

		top.geometry("483x467+574+186")
		top.title("New Toplevel")
		top.configure(background="#d9d9d9")
		top.configure(highlightbackground="#d9d9d9")
		top.configure(highlightcolor="black")



		self.Canvas1 = Canvas(top)
		self.Canvas1.place(relx=0.58, rely=0.13, relheight=0.52, relwidth=0.38)
		self.Canvas1.configure(background="#d9d9d9")
		self.Canvas1.configure(borderwidth="2")
		self.Canvas1.configure(highlightbackground="#d9d9d9")
		self.Canvas1.configure(highlightcolor="black")
		self.Canvas1.configure(insertbackground="black")
		self.Canvas1.configure(relief=RIDGE)
		self.Canvas1.configure(selectbackground="#c4c4c4")
		self.Canvas1.configure(selectforeground="black")
		self.Canvas1.configure(width=183)


		self.titleVar = Text(top)
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
		self.titleVar.configure(wrap=WORD)

		self.genreVar = Text(top)
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
		self.genreVar.configure(wrap=WORD)

		self.bindingVar = Text(top)
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
		self.bindingVar.configure(wrap=WORD)

		self.ageVar = Text(top)
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
		self.ageVar.configure(wrap=WORD)

		self.Text7 = Text(top)
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
		self.Text7.configure(wrap=WORD)

		self.blurbVar = Text(top)
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
		self.blurbVar.configure(wrap=WORD)

		self.title = Label(top)
		self.title.place(relx=0.06, rely=0.06, height=21, width=35)
		self.title.configure(activebackground="#f9f9f9")
		self.title.configure(activeforeground="black")
		self.title.configure(background="#d9d9d9")
		self.title.configure(disabledforeground="#a3a3a3")
		self.title.configure(foreground="#000000")
		self.title.configure(highlightbackground="#d9d9d9")
		self.title.configure(highlightcolor="black")
		self.title.configure(text='''Title:''')

		self.Label2 = Label(top)
		self.Label2.place(relx=0.04, rely=0.15, height=21, width=52)
		self.Label2.configure(activebackground="#f9f9f9")
		self.Label2.configure(activeforeground="black")
		self.Label2.configure(background="#d9d9d9")
		self.Label2.configure(disabledforeground="#a3a3a3")
		self.Label2.configure(foreground="#000000")
		self.Label2.configure(highlightbackground="#d9d9d9")
		self.Label2.configure(highlightcolor="black")
		self.Label2.configure(text='''Author:''')

		self.Label3 = Label(top)
		self.Label3.place(relx=0.06, rely=0.24, height=21, width=50)
		self.Label3.configure(activebackground="#f9f9f9")
		self.Label3.configure(activeforeground="black")
		self.Label3.configure(background="#d9d9d9")
		self.Label3.configure(disabledforeground="#a3a3a3")
		self.Label3.configure(foreground="#000000")
		self.Label3.configure(highlightbackground="#d9d9d9")
		self.Label3.configure(highlightcolor="black")
		self.Label3.configure(text='''Genre:''')

		self.Label4 = Label(top)
		self.Label4.place(relx=0.0, rely=0.32, height=21, width=85)
		self.Label4.configure(activebackground="#f9f9f9")
		self.Label4.configure(activeforeground="black")
		self.Label4.configure(background="#d9d9d9")
		self.Label4.configure(disabledforeground="#a3a3a3")
		self.Label4.configure(foreground="#000000")
		self.Label4.configure(highlightbackground="#d9d9d9")
		self.Label4.configure(highlightcolor="black")
		self.Label4.configure(text='''Released:''')

		self.Label5 = Label(top)
		self.Label5.place(relx=0.02, rely=0.41, height=21, width=53)
		self.Label5.configure(activebackground="#f9f9f9")
		self.Label5.configure(activeforeground="black")
		self.Label5.configure(background="#d9d9d9")
		self.Label5.configure(disabledforeground="#a3a3a3")
		self.Label5.configure(foreground="#000000")
		self.Label5.configure(highlightbackground="#d9d9d9")
		self.Label5.configure(highlightcolor="black")
		self.Label5.configure(text='''Binding:''')

		self.Label6 = Label(top)
		self.Label6.place(relx=0.06, rely=0.49, height=21, width=36)
		self.Label6.configure(activebackground="#f9f9f9")
		self.Label6.configure(activeforeground="black")
		self.Label6.configure(background="#d9d9d9")
		self.Label6.configure(disabledforeground="#a3a3a3")
		self.Label6.configure(foreground="#000000")
		self.Label6.configure(highlightbackground="#d9d9d9")
		self.Label6.configure(highlightcolor="black")
		self.Label6.configure(text='''Age:''')

		self.Label7 = Label(top)
		self.Label7.place(relx=0.06, rely=0.58, height=21, width=37)
		self.Label7.configure(activebackground="#f9f9f9")
		self.Label7.configure(activeforeground="black")
		self.Label7.configure(background="#d9d9d9")
		self.Label7.configure(disabledforeground="#a3a3a3")
		self.Label7.configure(foreground="#000000")
		self.Label7.configure(highlightbackground="#d9d9d9")
		self.Label7.configure(highlightcolor="black")
		self.Label7.configure(text='''Label:''')

		self.Label8 = Label(top)
		self.Label8.place(relx=0.06, rely=0.69, height=21, width=37)
		self.Label8.configure(activebackground="#f9f9f9")
		self.Label8.configure(activeforeground="black")
		self.Label8.configure(background="#d9d9d9")
		self.Label8.configure(disabledforeground="#a3a3a3")
		self.Label8.configure(foreground="#000000")
		self.Label8.configure(highlightbackground="#d9d9d9")
		self.Label8.configure(highlightcolor="black")
		self.Label8.configure(text='''Blurb:''')

		self.releasedVar = Text(top)
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
		self.releasedVar.configure(wrap=WORD)

		self.authorVar = Text(top)
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
		self.authorVar.configure(wrap=WORD)
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


		self.titleVar.insert(INSERT, title)
		self.authorVar.insert(INSERT, author)
		self.genreVar.insert(INSERT, genre)
		self.releasedVar.insert(INSERT, released)
		self.bindingVar.insert(INSERT, binding)
		self.ageVar.insert(INSERT,age)
		self.Text7.insert(INSERT, label)
		self.blurbVar.insert(INSERT, blurb)
		if imgURL == img.imgGet():
			photo = Tk.PhotoImage(imgURL)
		else:
			urllib.request.urlretrieve(imgURL, "D:/pyscripter/pycharm/projects/bookworm/image.jpg")
			#fp = open("D:/pyscripter/pycharm/projects/bookworm/image.jpg")
			picture = pict.open("D:/pyscripter/pycharm/projects/bookworm/image.jpg")
			photo = ImageTk.PhotoImage(picture)
		#photo = ImageTk.PhotoImage(imgURL)
		self.Canvas1.create_image(0,0, photo, NW)
		#self.Canvas1.pack()







if __name__ == '__main__':
	vp_start_gui()



