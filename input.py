import entrysmall
import entrysmall_support
import book
import book_support
import tkinter
import sqlite3
import entry
import sql
import books_api as books
import book2


def isbn():
	root = tkinter.Tk()
	#entrysmall_support.set_Tk_var("Enter the ISBN:")
	top = entrysmall.Entry_Form(root, entry = str("isbn:"))
	entrysmall_support.init(root, top)
	root.mainloop()

def bookDeets(j, k, l, m, n, o, p, q, r):
	'''
	root = tkinter.Tk()
	top = book.New_Toplevel(root, j, k, l, m, n, o, p, q, r)
	book_support.init(root, top)
	root.resizable(False, False)
	root.mainloop()
	'''
	book2.Book(j, k, l, m, n, o, p, q, r)


def isbn2book():
	entry.App("isbn here:")
	isbn = sql.dbInputOut()
	#print(len(isbn))
	if isbn == "":
		print("error")
	elif len(isbn) == 13:
		j, k, l, m, n, o, p, q, r = books.getAll(books.getBook(isbn))
		bookDeets(j, k, l, m, n, o, p, q, r, isbn)
	elif len(isbn) == 10:
		j, k, l, m, n, o, p, q, r = books.getAll(books.getBook(isbn))
		bookDeets(j, k, l, m, n, o, p, q, r, isbn)
	else:
		print("error")