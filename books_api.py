import googlebooks

def getNewBook(isbn1 = None):
	null = {'kind': 'books#volumes', 'totalItems': 0}
	api = googlebooks.Api()
	isbn = "isbn:"
	if isbn1 == None:
		isbn += input("input isbn")
		isbn1 = isbn
	else:
		isbn += isbn1
		isbn1 = isbn
	raw = "<Response [403]>"
	deets = {}
	raw = api.list(isbn1)
	while str(raw) == "<Response [403]>":
		raw = api.list(isbn1)
		try:
			deets = dict(raw)
		except ValueError:
			print(raw)
	# print(deets)
	if deets == null:
		return deets
		# ask entry for sql database
	else:
		return deets

def get_all_new(isbn):
	deets = getNewBook(isbn)
	new_data = []
	for t in "title", "authors", "categories", "publishedDate", "maturityRating", "description":
		try:
			data = deets["items"][0]["volumeInfo"][t]
			if isinstance(data, list):
				data2 = ""
				for i in range(len(list(data))):
					data2 += str(data[i])
					if i != len(list(data))-1:
						data2 += ", "
				data = data2
			new_data.append(data)
		except KeyError:
			new_data.append("Unknown")
	new_data.append(get_single_deet(isbn, "thumbnail"))

	a = new_data[0]  # title
	b = new_data[1]  # author
	c = new_data[2]  # genre
	d = new_data[3]  # released date
	e = None
	f = new_data[4]  # age rating
	g = None
	h = new_data[5]  # blurb
	i = new_data[6]  # image url
	return a, b, c, d, e, f, g, h, i


def get_single_deet(isbn, type):
	"""
	:param isbn:
	:param type: title, authors, description, categories, publishedDate, maturityRating, thumbnail
	:return:
	"""
	deets = getNewBook(isbn)
	null = {'kind': 'books#volumes', 'totalItems': 0}
	if deets != null:
		try:
			if type != "thumbnail":
				data = deets["items"][0]["volumeInfo"][type]
				if isinstance(data, list):
					data2 = ""
					for i in range(len(list(data))):
						data2 += str(data[i])
						if i != len(list(data))-1:
							data2 += ", "
					data = data2
			else:
				data = deets["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
				# print(data)
		except KeyError:
			data = "Unknown"
	else:
		data = "Unknown"
	return data







