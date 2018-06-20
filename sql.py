import sqlite3


def dbInputIn(input1):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	cmd = str("INSERT INTO input VALUES (\"")
	cmd += str(input1)
	cmd += str(chr(34))
	cmd += str(chr(41))
	#print(cmd)
	c.execute(cmd)
	conn.commit()
	conn.close()


def dbInputOutAll():
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	c.execute("SELECT * FROM input")
	data = c.fetchall()
	conn.close()
	#return data
	final = []
	for count in range(len(data)):
		value = str(data[count])
		real = value[2:len(value)-3]
		print(real)
		final.append(real)
	return final


def dbInputOut():
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	c.execute("SELECT * FROM input")
	data = c.fetchall()
	conn.close()
	# return data
	value = str(data[len(data)-1])
	real = value[2:len(value) - 3]
	return real


def checkBook(isbn):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
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

def addBook(a, b, c, d, e, f, g, h, i, j):
	#compare to google books then update sql


def getBook(isbn):
	conn = sqlite3.connect("D:/pyscripter/pycharm/projects/bookworm/database/database.db")
	c = conn.cursor()
	cmd = str("SELECT * FROM changed_books WHERE isbn = (\"")
	cmd += str(isbn)
	cmd += str(chr(34))
	cmd += str(chr(41))
	c.execute(cmd)
	data = str(c.fetchall())
	conn.close()

	a = data[2:data.find(",")]
	data = data[data.find(",") + 2:]
	b = data[:data.find(",")]
	data = data[data.find(",") + 2:]
	c = data[:data.find(",")]
	data = data[data.find(",") + 2:]
	d = data[:data.find(",")]
	data = data[data.find(",") + 2:]
	e = data[:data.find(",")]
	data = data[data.find(",") + 2:]
	f = data[:data.find(",")]
	data = data[data.find(",") + 2:]
	g = data[:data.find(",")]
	data = data[data.find(",") + 2:]
	h = data[:data.find(",")]
	data = data[data.find(",") + 2:]
	i = data[:data.find(",")]
	data = data[data.find(",") + 2:]
	j = data[:len(data)-2]

	return a, b, c, d, e, f, g, h, i, j
