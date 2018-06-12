import books_api as books
import unknown
import unknown_support
import tkinter

if __name__ == "__main__":
	isbn = 9781910523117
	j,k,l,m,n,o,p,q,r = books.getAll(books.getBook(isbn))
	books.printAll(j,k,l,m,n,o,p,q,r)
	url = books.getImageURL(books.getBook(isbn))
	books.imgUrl(url)
	root = tkinter.Tk()
	top = unknown.New_Toplevel(root, j, k, l, m, n, o, p, q, r)
	unknown_support.init(root, top)
	root.mainloop()
