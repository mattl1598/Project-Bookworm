import entrysmall
import entrysmall_support
import book
import book_support
import tkinter
import sqlite3
import entry


def isbn():
	root = tkinter.Tk()
	#entrysmall_support.set_Tk_var("Enter the ISBN:")
	top = entrysmall.Entry_Form(root, entry = str("isbn:"))
	entrysmall_support.init(root, top)
	root.mainloop()


def isbn2():
	isbn1 = entrysmall.Entry_Form()
	return isbn1


def bookDeets(j, k, l, m, n, o, p, q, r):
	root = tkinter.Tk()
	top = book.New_Toplevel(root, j, k, l, m, n, o, p, q, r)
	book_support.init(root, top)
	root.resizable(False, False)
	root.mainloop()

def isbn2book():
	entry.App("isbn here:")