<<<<<<< HEAD
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

def bookDeets(j, k, l, m, n, o, p, q, r, isbn):
	'''
	root = tkinter.Tk()
	top = book.New_Toplevel(root, j, k, l, m, n, o, p, q, r)
	book_support.init(root, top)
	root.resizable(False, False)
	root.mainloop()
	'''
	book2.Book(j, k, l, m, n, o, p, q, r, isbn)


def isbn2book():
	entry.App("isbn here:")
	isbn = sql.dbInputOut()
	#print(len(isbn))
	if len(isbn) == 13 or len(isbn) == 10:
		if sql.inDB(isbn) == True:
			isbn, j, k, l, m, n, o, p, q, r = sql.getBook(isbn)
			print(j, k, l, m, n, o, p, q, r, isbn)
			#print("sql")
		else:
			j, k, l, m, n, o, p, q, r = books.getAll(books.getBook(isbn))
			#print("books")
			print(j, k, l, m, n, o, p, q, r, isbn)
		bookDeets(j, k, l, m, n, o, p, q, r, isbn)
	else:
=======
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

def bookDeets(j, k, l, m, n, o, p, q, r, isbn):
	'''
	root = tkinter.Tk()
	top = book.New_Toplevel(root, j, k, l, m, n, o, p, q, r)
	book_support.init(root, top)
	root.resizable(False, False)
	root.mainloop()
	'''
	book2.Book(j, k, l, m, n, o, p, q, r, isbn)


def isbn2book():
	entry.App("isbn here:")
	isbn = sql.dbInputOut()
	#print(len(isbn))
	if len(isbn) == 13 or len(isbn) == 10:
		if sql.inDB(isbn) == True:
			isbn, j, k, l, m, n, o, p, q, r = sql.getBook(isbn)
			print(j, k, l, m, n, o, p, q, r, isbn)
			#print("sql")
		else:
			j, k, l, m, n, o, p, q, r = books.getAll(books.getBook(isbn))
			#print("books")
			print(j, k, l, m, n, o, p, q, r, isbn)
		bookDeets(j, k, l, m, n, o, p, q, r, isbn)
	else:
>>>>>>> ade12e8163ce3463b78236abe5051e4cc8d5d57b
		print("error")