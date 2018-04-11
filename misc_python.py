#-------------------------------------------------------------------------------
# Name:        misc_python
# Purpose:     misc python utilities
#
# Author:      matthewl9
#
# Version:     0.1
#
# Contains:    
#	       Functions: write to file, quicksort, import_list, check file, find mid
#	       Classes: stack
#
# Created:     21/02/2018
# Copyright:   (c) matthewl9 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class stack():
	top = 0
	stack = []
	isEmpty = True
	isFull = False

	def __init__(self):
		self.top = 0
		self.stack = []
		self.isEmpty = True
		self.isFull = False

	def add(self,data):
		self.isEmpty = False
		self.top++1
		self.stack.append(data)

	def pop(self):
		data = self.stack.pop(top)
		self.top--1
		return(data)

def write(filepath, list1):                      #writes to file
	filepath = str(filepath)
	file = open(filepath,"w")
	for count in range (len(list1)):
		file.write(str(list1[count]))
		if count < (len(list1)-1) and count > 0:
			file.write("\n")
	file.close

def partition(data):
  pivot = data[0]
  less, equal, greater = [], [], []
  for temp in data:
   if temp < pivot:
    less.append(temp)
   elif temp > pivot:
    greater.append(temp)
   else:
    equal.append(temp)
  return less, equal, greater

def quicksort(data):                             #quicksort algorithm. takes list
  if data:
   less, equal, greater = partition(data)
   return quicksort(less) + equal + quicksort(greater)
  return data

def checkFile(filepath):
	working = False
	try:
		txt = open(filepath)
		txt.close()
		working = True
	except:
		length = len(filepath)
		working = False
		shortFile = filepath[1:length]
		letters = []
		for i in range(25):
			letters.append(chr(i+65))
		while working == False:
			for i in range(25):
				trying = letters[i] + shortFile
				print(trying)
				try:
					txt = open(trying, "r")
					txt.close()
					working = True
					break
				except:
					working = False
			break
		filepath = trying
	return(filepath)



def import_list(filepath):               #imports list from file
	file = checkFile(filepath)
	txt = open(file, "r")
	shuff = txt.read().splitlines()
	txt.close()
	return(shuff)

def sortFromToFile(infile, outfile, debug):      #takes in file, writes sorted list to another file
	postsort = sortFromFile(infile,debug)
	write(outfile, postsort)
	if debug == True:
		print("Written:", len(postsort), "words.")

def sortFromFile(infile,debug):                   #takes in file, returns sorted list
	shuff = import_list(infile)
	postsort = quicksort(shuff)
	#write(outfile, postsort)
	if debug == True:
		print("Sorted:", len(postsort), "words.")
	return(postsort)

def search(string, data):
	return(string in data)

def gethalf(sort, uppervalue):
	print()

def binSearch(string,data):
	sort = data
	lowervalue = int(0)
	uppervalue = int(len(sort))
	found = False
	count = 0
	while found == False:
		#print(count)
		#count = count + 1
		#print(lowervalue, " ", uppervalue)
		halfway = ((uppervalue - lowervalue)//2) + lowervalue
		if string >= sort[halfway]:
			lowervalue = halfway
		else:
			uppervalue = halfway
		if uppervalue == lowervalue or uppervalue == lowervalue + 1:
			location = int(lowervalue)
			print(location)
			found = True
	return(location, data[location])

def FindMid(list1):
	length = len(list1)
	mid = length//2
	return mid


