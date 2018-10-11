import sqlite3
import books_api as books
import misc_python as misc

<<<<<<< HEAD
def db_input_in(input1):
=======

def dbInputIn(input1):
>>>>>>> 77d70087116cb3542db994ff5dd771921a03de6f
	conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
	c = conn.cursor()
	cmd = str("INSERT INTO input VALUES (\"")
	cmd += str(input1)
	cmd += str(chr(34))
	cmd += str(chr(41))
	c.execute(cmd)
	conn.commit()
	conn.close()


<<<<<<< HEAD
def db_input_out_all():
=======
def dbInputOutAll():
>>>>>>> 77d70087116cb3542db994ff5dd771921a03de6f
	conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
	c = conn.cursor()
	c.execute("SELECT * FROM input")
	data = c.fetchall()
	conn.close()
	final = []
	for count in range(len(data)):
		value = str(data[count])
		real = value[2:len(value)-3]
		print(real)
		final.append(real)
	return final


<<<<<<< HEAD
def db_input_out():
=======
def dbInputOut():
>>>>>>> 77d70087116cb3542db994ff5dd771921a03de6f
	conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
	c = conn.cursor()
	c.execute("SELECT * FROM input")
	data = c.fetchall()
	conn.close()
	# return data
	value = str(data[len(data)-1])
	real = value[2:len(value) - 3]
	return real


<<<<<<< HEAD
def check_book(isbn):
=======
def checkBook(isbn):
>>>>>>> 77d70087116cb3542db994ff5dd771921a03de6f
	conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
	c = conn.cursor()
	cmd = str("SELECT * FROM changed_books WHERE isbn = (\"")
	cmd += str(isbn)
	cmd += str(chr(34))
	cmd += str(chr(41))
	c.execute(cmd)
	data = c.fetchall()
	conn.close()
	print(data)
	if data == "[]":
		return False
	else:
		return True


def add_book(isbn, a, b, c, d, e, f, g, h, i):
	# compare to google books then update sql
	a1, b1, c1, d1, e1, f1, g1, h1, i1 = books.getAll(isbn)
	if a == a1:
		a = "None"
	if b == b1:
		b = "None"
	elif b == "":
		b = "None"
	if c == c1:
		c = "None"
	elif c == "":
		c = "None"
	if d == d1:
		d = "None"
	if e == e1:
		e = "None"
	if f == f1:
		f = "None"
	if g == g1:
		g = "None"
	if h == h1:
		h = "None"
	if i == i1:
		i = "None"
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	cur = conn.cursor()
	if check_book(isbn) is True:
		cur.execute("DELETE FROM changed_books WHERE isbn = ?", (isbn,))
	cur.execute("INSERT INTO changed_books (isbn, title, author, genre, released, binding, age, label, blurb) VALUES "
				"(?, ?, ?, ?, ?, ?, ?, ?, ?)",
				(isbn, str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h),))
	conn.commit()
	conn.close()

<<<<<<< HEAD

def in_db(isbn):
=======
def inDB(isbn):
>>>>>>> 77d70087116cb3542db994ff5dd771921a03de6f
	conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
	c = conn.cursor()
	cmd = str("SELECT isbn FROM changed_books")
	c.execute(cmd)
	data = str(c.fetchall())
	conn.close()
	return str(isbn) in data


<<<<<<< HEAD
def get_book(isbn):
	conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
	c = conn.cursor()
	cmd = str("SELECT * FROM changed_books WHERE isbn = (\"")
	cmd += str(isbn)
	cmd += str(chr(34))
	cmd += str(chr(41))
	c.execute(cmd)
	data = str(c.fetchall())
	conn.close()

	a = data[2:data.find(",")]
	data = data[data.find(",") + 3:]

	b = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]

	c = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]

	d = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]

	e = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]

	f = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]

	g = data[:data.find(",") - 3]
	data = data[data.find(",") + 3:]

	h = data[:data.find(",") - 3]
	data = data[data.find(", \"") + 3:]

	i = data[:data.find("\",") - 2]
	data = data[data.find(",") + 3:]

	j = data[:len(data) - 1]

	return a, b, c, d, e, f, g, h, i, j


def get_schools():
	conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
	c = conn.cursor()
	cmd = "SELECT name FROM schools;"
	c.execute(cmd)
	data = c.fetchall()
	conn.close()

	conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
	c = conn.cursor()
	cmd = "SELECT name, school_id FROM schools;"
	c.execute(cmd)
	data2 = dict(c.fetchall())
	conn.close()

	data3 = []
	for i in range(len(data)):
		data3.append(data[i][0])

	data4 = misc.better_sort(data3)

	print(data4)

	#names = []

	# for i in range(len(data)):
	#	names.append(data[i])

	return data2, data, data4


def get_school_deets(school_id):
	conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
	c = conn.cursor()
	cmd = "SELECT * FROM schools WHERE school_id = "
	cmd += str(school_id)
	cmd += ";"
	c.execute(cmd)
	raw = c.fetchall()
	values = list(raw[0])
	conn.close()

=======
def getBook(isbn):
>>>>>>> 77d70087116cb3542db994ff5dd771921a03de6f
	conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
	c = conn.cursor()
	cmd = "SELECT * FROM schools;"
	c.execute(cmd)
	keys = [description[0] for description in c.description]
	conn.close()

	out = create_dict(keys, values)

<<<<<<< HEAD
	return out


def new_school(data):
	new_id = 0
	data2 = data

	worked = False

	while worked is False:
		print(data2)
		data = data2
		try:
			conn = sqlite3.connect("D:\Project-Bookworm\database\database.db")
			c = conn.cursor()
			data.insert(0, str(new_id))
			print(data)
			cmd = '''INSERT INTO schools(school_id, name, HT, lastEx, Contact, DFE, address) VALUES(?,?,?,?,?,?,?)'''
			c.execute(cmd, tuple(data))
			conn.commit()
			conn.close()
			worked = True
			print("worked")
		except sqlite3.IntegrityError:
			new_id = new_id + 1
			print("test")
		except sqlite3.ProgrammingError:
			data.pop(0)
			data.pop(0)

	return new_id


def create_dict(keys, values):
	return dict(zip(keys, values + [None] * (len(keys) - len(values))))
=======
	return a, b, c, d, e, f, g, h, i, j
>>>>>>> 77d70087116cb3542db994ff5dd771921a03de6f
