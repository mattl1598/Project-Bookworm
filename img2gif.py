from PIL import Image
import sys
import os
from win32com.shell import shell, shellcon

def main():
	#im = Image.open("D:/pyscripter/pycharm/projects/bookworm/image.jpg")
	docs = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
	infile = docs + "\\Project-Bookworm\\image.jpg"
	outfile = docs + "\\Project-Bookworm\\image.gif"
	#print(im.format, im.size, im.mode)
	f, e = os.path.splitext(infile)
	outfile = f + ".gif"
	Image.open(infile).save(outfile, 'gif')
	im = Image.open(docs + "\\Project-Bookworm\\image.gif")
	#print(im.format, im.size, im.mode)


def error():
	#im = Image.open("D:/pyscripter/pycharm/projects/bookworm/error.jpg")
	docs = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
	infile = docs+"\\Project-Bookworm\\error.jpg"
	outfile = docs+"\\Project-Bookworm\\error.gif"
	#print(im.format, im.size, im.mode)
	f, e = os.path.splitext(infile)
	outfile = f + ".gif"
	Image.open(infile).save(outfile, 'gif')
	im = Image.open("D:\Project-Bookworm\error.gif")
	#print(im.format, im.size, im.mode)


def resize():
	basewidth = 183
	docs = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
	img = Image.open(docs + '\\Project-Bookworm\\image.gif')
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
	img.save(docs+'\\Project-Bookworm\\image.gif')


def resizeError():
	basewidth = 183
	docs = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
	img = Image.open(docs + '\\Project-Bookworm\error.gif')
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
