<<<<<<< HEAD
import books_api as books
import book
import book_support
import tkinter
import entrysmall
import input
import entry
import sql


if __name__ == "__main__":
	'''
	isbn = 1509860142
	j, k, l, m, n, o, p, q, r = books.getAll(books.getBook(isbn))
	books.printAll(j, k, l, m, n, o, p, q, r)
	url = books.getImageURL(books.getBook(isbn))
	books.imgUrl(url)
	#input.bookDeets(j, k, l, m, n, o, p, q, r)
	
	root = tkinter.Tk()
	top = book.New_Toplevel(root, j, k, l, m, n, o, p, q, r)
	book_support.init(root, top)
	root.resizable(False, False)
	root.mainloop()'''
	input.isbn2book()

	#print(sql.getBook(1509860142))
	#print(sql.inDB(1509860142))
=======
import books_api as books
import book
import book_support
import tkinter
import entrysmall
import input
import entry
import sql


if __name__ == "__main__":
	'''
	isbn = 1509860142
	j, k, l, m, n, o, p, q, r = books.getAll(books.getBook(isbn))
	books.printAll(j, k, l, m, n, o, p, q, r)
	url = books.getImageURL(books.getBook(isbn))
	books.imgUrl(url)
	#input.bookDeets(j, k, l, m, n, o, p, q, r)
	
	root = tkinter.Tk()
	top = book.New_Toplevel(root, j, k, l, m, n, o, p, q, r)
	book_support.init(root, top)
	root.resizable(False, False)
	root.mainloop()'''
	input.isbn2book()

	#print(sql.getBook(1509860142))
	#print(sql.inDB(1509860142))
>>>>>>> ade12e8163ce3463b78236abe5051e4cc8d5d57b
