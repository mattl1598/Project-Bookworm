import sqlite3
import books_api as books
import misc_python as misc
import json
import time
from win32com.shell import shell, shellcon

def get_db():
	docs = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
	setts = docs + "\\GitHub\\Project-Bookworm\\settings.json"
	with open(setts, "r") as file:
		settings = json.load(file)

	db = settings["database_location"]

	return db

# reports sql

def create_tables():
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	books = str("""CREATE TABLE "books" ( `isbn` TEXT NOT NULL, `copy_no` INTEGER NOT NULL, `loan_id` INTEGER, 
	PRIMARY KEY(`isbn`,`copy_no`), 
	FOREIGN KEY(`loan_id`) 
	REFERENCES `loans`(`loan_id`) )""")
	changed_books = str("""CREATE TABLE "changed_books" ( `isbn` TEXT NOT NULL UNIQUE, `title` TEXT, `author` TEXT, 
	`genre` TEXT, `released` TEXT, `binding` TEXT, `age` TEXT, 
	`label` TEXT, `blurb` TEXT, `image` BLOB, 
	PRIMARY KEY(`isbn`) )""")
	loans = str("""CREATE TABLE "loans" ( `loan_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, 
	`dates` TEXT NOT NULL, `school_id` INTEGER NOT NULL, `active` TEXT NOT NULL, 
	FOREIGN KEY(`school_id`) 
	REFERENCES `schools`(`school_id`) )""")
	login = str("""CREATE TABLE "login" ( `userID` INTEGER NOT NULL UNIQUE, `username` TEXT NOT NULL UNIQUE, 
	`password` TEXT NOT NULL, `isDepressed` TEXT NOT NULL, 
	PRIMARY KEY(`userID`) )""")
	schools = str("""CREATE TABLE "login" ( `userID` INTEGER NOT NULL UNIQUE, `username` TEXT NOT NULL UNIQUE, 
	`password` TEXT NOT NULL, `isDepressed` TEXT NOT NULL, PRIMARY KEY(`userID`) )""")
	c.execute(books)
	conn.commit()
	c.execute(changed_books)
	conn.commit()
	c.execute(loans)
	conn.commit()
	c.execute(login)
	conn.commit()
	c.execute(schools)
	conn.commit()
	conn.close()
	new_user("admin", "password", "True")


def get_books_location(location):
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = str("""SELECT books.isbn, books.copy_no, schools.name
FROM books
LEFT JOIN loans
ON books.loan_id = loans.loan_id
LEFT JOIN schools
ON loans.school_id = schools.school_id
WHERE schools.school_id = ?
ORDER BY books.isbn, books.copy_no;""")
	c.execute(cmd, (location,))
	data = c.fetchall()
	conn.close()
	return data

def get_copys_location(location, isbn):
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = str("""SELECT books.isbn, books.copy_no, schools.name
FROM books
LEFT JOIN loans
ON books.loan_id = loans.loan_id
LEFT JOIN schools
ON loans.school_id = schools.school_id
WHERE schools.school_id = ? AND books.isbn = ?
ORDER BY books.isbn, books.copy_no;""")
	c.execute(cmd, (location, isbn,))
	data = c.fetchall()
	conn.close()
	return data

def send_books(books, loan_id):
	db = get_db()
	copy = []
	for count in range(len(books)):
		isbn = books[count]
		data = get_copys_location(0, isbn)
		print(data)
		copy.append(list(data[0])[1])

	cmd = "UPDATE books SET loan_id = ? WHERE isbn = ? AND copy_no = ?;"
	conn = sqlite3.connect(db)
	c = conn.cursor()

	for count in range(len(books)):
		c.execute(cmd, (loan_id, books[count], copy[count],))

	conn.commit()
	conn.close()


def create_new_loan(loc):
	date = str(time.strftime("%d/%m/%Y"))
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = str("""INSERT INTO loans(school_id, dates, active) VALUES (?, ?, "True"); """)
	c.execute(cmd, (loc, date,))
	conn.commit()
	cmd2 = str("SELECT loan_id FROM loans;")
	c.execute(cmd2)
	data = c.fetchall()
	conn.close()
	data2 = sorted(data)
	print(data2)
	value = data2[len(data2)-1][0]
	print(value)
	return value


def get_logins():
	db = get_db()
	connected = False
	while connected is False:
		try:
			conn = sqlite3.connect(db)
			connected = True
		except sqlite3.OperationalError:
			pass # create database
	c = conn.cursor()
	cmd = str("SELECT * FROM login")
	c.execute(cmd)
	data = c.fetchall()
	conn.close()
	return data

def get_locations():
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = str("SELECT school_id, name FROM schools")
	c.execute(cmd)
	data = c.fetchall()
	conn.close()
	return data

def new_user(a, b, c):
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = str("INSERT INTO login (username, password, isDepressed) VALUES (?,?,?)")
	c.execute(cmd, (str(a), str(b), str(c)))
	conn.commit()
	conn.close()

def db_input_in(input1):
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = str("INSERT INTO input VALUES (\"")
	cmd += str(input1)
	cmd += str(chr(34))
	cmd += str(chr(41))
	c.execute(cmd)
	conn.commit()
	conn.close()


def db_input_out_all():
	db = get_db()
	conn = sqlite3.connect(db)
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


def db_input_out():
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("SELECT * FROM input")
	data = c.fetchall()
	conn.close()
	# return data
	value = str(data[len(data)-1])
	real = value[2:len(value) - 3]
	return real


def check_book(isbn):
	db = get_db()
	conn = sqlite3.connect(db)
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
	db = get_db()
	# compare to google books then update sql
	a1, b1, c1, d1, e1, f1, g1, h1, i1 = books.get_all_new(isbn)
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
	conn = sqlite3.connect(db)
	cur = conn.cursor()
	if check_book(isbn) is True:
		cur.execute("DELETE FROM changed_books WHERE isbn = ?", (isbn,))
	cur.execute("INSERT INTO changed_books (isbn, title, author, genre, released, binding, age, label, blurb) VALUES "
				"(?, ?, ?, ?, ?, ?, ?, ?, ?)",
				(isbn, str(a), str(b), str(c), str(d), str(e), str(f), str(g), str(h),))
	conn.commit()
	conn.close()


def in_db(isbn):
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = str("SELECT isbn FROM changed_books")
	c.execute(cmd)
	data = str(c.fetchall())
	conn.close()
	return str(isbn) in data


def get_book(isbn):
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = str("SELECT * FROM changed_books WHERE isbn = (\"")
	cmd += str(isbn)
	cmd += str(chr(34))
	cmd += str(chr(41))
	c.execute(cmd)
	data = c.fetchall()
	conn.close()

	# print(data)

	a = data[0][0]
	b = data[0][1]
	c = data[0][2]
	d = data[0][3]
	e = data[0][4]
	f = data[0][5]
	g = data[0][6]
	h = data[0][7]
	i = data[0][8]
	j = data[0][9]

	return a, b, c, d, e, f, g, h, i, j


def get_schools():
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = "SELECT name FROM schools;"
	c.execute(cmd)
	data = c.fetchall()
	conn.close()

	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = "SELECT name, school_id FROM schools;"
	c.execute(cmd)
	data2 = dict(c.fetchall())
	conn.close()

	data3 = []
	for i in range(len(data)):
		data3.append(data[i][0])

	data4 = misc.better_sort(data3)

	# print(data4)

	# names = []

	# for i in range(len(data)):
	# 	names.append(data[i])

	return data2, data, data4

def get_school_id(name):
	pass



def get_school_deets(school_id):
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = "SELECT * FROM schools WHERE school_id = "
	cmd += str(school_id)
	cmd += ";"
	c.execute(cmd)
	raw = c.fetchall()
	values = list(raw[0])
	conn.close()

	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = "SELECT * FROM schools;"
	c.execute(cmd)
	keys = [description[0] for description in c.description]
	conn.close()

	out = create_dict(keys, values)
	return out


def new_school(data):
	db = get_db()
	new_id = 0
	data2 = data

	worked = False

	while worked is False:
		print(data2)
		data = data2
		try:
			conn = sqlite3.connect(db)
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


def edit_school(sch_id, data):
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	names = ["school_id", "name", "HT", "lastEx", "Contact", "DFE", "pupilTotal", "itemsPer", "address"]
	cmd = '''UPDATE schools SET '''
	for i in range(6):
		cmd += names[i+1]
		cmd += " = \""
		cmd += data[i]
		if i == 5:
			cmd += "\""
		else:
			cmd += "\", "
	cmd += " WHERE school_id = \""
	cmd += str(sch_id)
	cmd += "\";"
	print(cmd)
	c.execute(cmd)
	conn.commit()
	conn.close()

def get_loans(school_id):
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = "SELECT loan_id FROM loans WHERE school_id = ?"
	c.execute(cmd, (school_id,))
	raw = c.fetchall()
	conn.close()
	data = list(raw[0])
	return data

def get_books_from_loan(loan_id):
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = "SELECT isbn FROM books WHERE loan_id = ?"
	c.execute(cmd, (loan_id,))
	raw = c.fetchall()
	print(raw)
	conn.close()
	data = []
	for i in range(len(raw)):
		data.append(raw[i][0])

	return data

def create_dict(keys, values):
	return dict(zip(keys, values + [None] * (len(keys) - len(values))))


