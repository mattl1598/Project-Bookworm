#-------------------------------------------------------------------------------
# Name:        books_api
# Purpose:
#
# Author:      mattl
#
# Created:     07/05/2018
# Copyright:   (c) mattl 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests # learn more: https://python.org/pypi/requests
import googlebooks
import misc_python
import urllib.request


def getBook(isbn1 = None):
	api = googlebooks.Api()
	isbn = "isbn:"
	if isbn1 == None:
		isbn += input("input isbn")
		isbn1 = isbn
	deets = api.list(isbn1)
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
	dataend = data.find("maturityRating") - 5
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

def imgUrl(url):
	#print(url)
	urllib.request.urlretrieve(url,"D:/pyscripter/pycharm/projects/bookworm/image.jpg")

def getAll(data):
	a = getTitle(data)
	b = getAuthor(data)
	c = getGenre(data)
	d = getReleased(data)
	e = None
	f = getAge(data)
	g = None
	h = getBlurb(data)
	i = getImageURL(data)
	return a,b,c,d,e,f,g,h,i

def printAll(a,b,c,d,e,f,g,h,i):
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)
	print(f)
	print(g)
	print(h)
	print(i)



