from PIL import Image
import sys
import os
import locations

def main():
	#im = Image.open("D:/pyscripter/pycharm/projects/bookworm/image.jpg")
	assets = locations.assets()
	infile = assets + "image.jpg"
	outfile = assets + "image.gif"
	#print(im.format, im.size, im.mode)
	f, e = os.path.splitext(infile)
	outfile = f + ".gif"
	Image.open(infile).save(outfile, 'gif')
	im = Image.open(assets + "image.gif")
	#print(im.format, im.size, im.mode)


def error():
	# im = Image.open("D:/pyscripter/pycharm/projects/bookworm/error.jpg")
	assets = locations.assets()
	infile = assets + "error.jpg"
	outfile = assets + "error.gif"
	#print(im.format, im.size, im.mode)
	f, e = os.path.splitext(infile)
	outfile = f + ".gif"
	Image.open(infile).save(outfile, 'gif')
	im = Image.open(assets + "error.gif")
	# print(im.format, im.size, im.mode)


def resize():
	basewidth = 183
	assets = locations.assets()
	img = Image.open(assets + 'image.gif')
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
	img.save(assets+'image.gif')


def resizeError():
	basewidth = 183
	assets = locations.assets()
	img = Image.open(assets + 'error.gif')
	wpercent = (basewidth / float(img.size[0]))
	hsize = int((float(img.size[1]) * float(wpercent)))
	img = img.resize((basewidth, hsize), Image.ANTIALIAS)
