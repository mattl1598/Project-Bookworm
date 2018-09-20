from PIL import Image
import sys
import os


def main():
	#im = Image.open("D:/pyscripter/pycharm/projects/bookworm/image.jpg")
	infile = "D:\Project-Bookworm\image.jpg"
	outfile = "D:\Project-Bookworm\image.gif"
	#print(im.format, im.size, im.mode)
	f, e = os.path.splitext(infile)
	outfile = f + ".gif"
	Image.open(infile).save(outfile, 'gif')
	im = Image.open("D:\Project-Bookworm\image.gif")
	#print(im.format, im.size, im.mode)


def error():
	#im = Image.open("D:/pyscripter/pycharm/projects/bookworm/error.jpg")
	infile = "D:\Project-Bookworm\error.jpg"
	outfile = "D:\Project-Bookworm\error.gif"
	#print(im.format, im.size, im.mode)
	f, e = os.path.splitext(infile)
	outfile = f + ".gif"
	Image.open(infile).save(outfile, 'gif')
	im = Image.open("D:\Project-Bookworm\error.gif")
	#print(im.format, im.size, im.mode)


def resize():
	basewidth = 183
	img = Image.open('D:\Project-Bookworm\image.gif')
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
	img.save('D:\Project-Bookworm\image.gif')


def resizeError():
	basewidth = 183
	img = Image.open('D:\Project-Bookworm\error.gif')
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
