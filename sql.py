import sqlite3
import books_api as books
import misc_python as misc
import json
import time

def get_db():

	with open("D:/Project-Bookworm/settings.json", "r") as file:
		settings = json.load(file)

	db = settings["database_location"]

	return db

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

def create_new_loan(loc):
	date = str(time.strftime("%d/%m/%Y"))
	db = get_db()
	conn = sqlite3.connect(db)
	c = conn.cursor()
	cmd = str("""INSERT INTO loans(school_id, dates, active) VALUES (?, ?, "True");""")
	c.execute(cmd, (loc, date,))
	cmd2 = "SELECT loan_id FROM loans;"
	c.execute(cmd2)
	data = c.fetchall()
	conn.commit()
	conn.close()
	return data


def get_logins():
	db = get_db()
	conn = sqlite3.connect(db)
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

	print(data)

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

	print(data4)

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




def create_dict(keys, values):
	return dict(zip(keys, values + [None] * (len(keys) - len(values))))

print(get_book("1509860142"))
