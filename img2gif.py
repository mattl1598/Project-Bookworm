<<<<<<< HEAD
from PIL import Image
import sys
import os


def main():
	#im = Image.open("D:/pyscripter/pycharm/projects/bookworm/image.jpg")
	infile = "D:/pyscripter/pycharm/projects/bookworm/image.jpg"
	outfile = "D:/pyscripter/pycharm/projects/bookworm/image.gif"
	#print(im.format, im.size, im.mode)
	f, e = os.path.splitext(infile)
	outfile = f + ".gif"
	Image.open(infile).save(outfile, 'gif')
	im = Image.open("D:/pyscripter/pycharm/projects/bookworm/image.gif")
	#print(im.format, im.size, im.mode)


def error():
	#im = Image.open("D:/pyscripter/pycharm/projects/bookworm/error.jpg")
	infile = "D:/pyscripter/pycharm/projects/bookworm/error.jpg"
	outfile = "D:/pyscripter/pycharm/projects/bookworm/error.gif"
	#print(im.format, im.size, im.mode)
	f, e = os.path.splitext(infile)
	outfile = f + ".gif"
	Image.open(infile).save(outfile, 'gif')
	im = Image.open("D:/pyscripter/pycharm/projects/bookworm/error.gif")
	#print(im.format, im.size, im.mode)


def resize():
	basewidth = 183
	img = Image.open('D:/pyscripter/pycharm/projects/bookworm/image.gif')
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
	img.save('D:/pyscripter/pycharm/projects/bookworm/image.gif')


def resizeError():
	basewidth = 183
	img = Image.open('D:/pyscripter/pycharm/projects/bookworm/error.gif')
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
=======
from PIL import Image
import sys
import os


def main():
	#im = Image.open("D:/pyscripter/pycharm/projects/bookworm/image.jpg")
	infile = "D:/pyscripter/pycharm/projects/bookworm/image.jpg"
	outfile = "D:/pyscripter/pycharm/projects/bookworm/image.gif"
	#print(im.format, im.size, im.mode)
	f, e = os.path.splitext(infile)
	outfile = f + ".gif"
	Image.open(infile).save(outfile, 'gif')
	im = Image.open("D:/pyscripter/pycharm/projects/bookworm/image.gif")
	#print(im.format, im.size, im.mode)


def error():
	#im = Image.open("D:/pyscripter/pycharm/projects/bookworm/error.jpg")
	infile = "D:/pyscripter/pycharm/projects/bookworm/error.jpg"
	outfile = "D:/pyscripter/pycharm/projects/bookworm/error.gif"
	#print(im.format, im.size, im.mode)
	f, e = os.path.splitext(infile)
	outfile = f + ".gif"
	Image.open(infile).save(outfile, 'gif')
	im = Image.open("D:/pyscripter/pycharm/projects/bookworm/error.gif")
	#print(im.format, im.size, im.mode)


def resize():
	basewidth = 183
	img = Image.open('D:/pyscripter/pycharm/projects/bookworm/image.gif')
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
	img.save('D:/pyscripter/pycharm/projects/bookworm/image.gif')


def resizeError():
	basewidth = 183
	img = Image.open('D:/pyscripter/pycharm/projects/bookworm/error.gif')
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
>>>>>>> ade12e8163ce3463b78236abe5051e4cc8d5d57b
	img.save('D:/pyscripter/pycharm/projects/bookworm/error.gif')