import googlebooks
import misc_python



def getBook():
	api = googlebooks.Api()
	isbn = "isbn:"
	isbn += input("input isbn")
	deets = api.list(isbn)
	return str(deets)


def getTitle(data):
	datastart = data.find('title') + 9
	dataend = data.find('authors') - 4
	return (data[datastart:dataend])


def getAuthor(data):
	datastart = data.find('authors') + 12
	dataend = data.find(']') - 1
	return (data[datastart:dataend])


def getGenre(data):
	datastart = data.find('categories') + 15
	dataend = data.find("averageRating") - 5
	return (data[datastart:dataend])


def getReleased(data):
	datastart = data.find('publishedDate') + 17
	dataend = data.find("description") - 4
	return (data[datastart:dataend])


#BINDING???


def getAge(data):
	datastart = data.find('maturityRating') + 18
	dataend = data.find("allowAnonLogging") - 4
	return (data[datastart:dataend])


def getBlurb(data):
	datastart = data.find('description') + 15
	dataend = data.find("industryIdentifiers") - 4
	return (data[datastart:dataend])


def getImageURL(data):
	datastart = data.find('thumbnail') + 13
	dataend = data.find("language") - 5
	return (data[datastart:dataend])



print(getTitle(getBook()))
