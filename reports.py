import tkinter
from win32com.shell import shell, shellcon
import json

def gettheme():
	docs = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0)
	setts = docs + "\\GitHub\\Project-Bookworm\\settings.json"
	with open(setts, "r") as read2:
		settings = json.load(read2)

	rootpath = settings["root_location"]

	with open(rootpath+"theme.json", "r") as readfile:
		theme1 = json.load(readfile)

	theme = theme1["theme"]

	bg = theme1[theme]["windows"]["background"]
	text = theme1[theme]["windows"]["text"]
	button_bg = theme1[theme]["button"]["background"]
	butt_txt = theme1[theme]["button"]["text"]
	box_bg = theme1[theme]["textbox"]["background"]
	box_txt = theme1[theme]["textbox"]["foreground"]
	cursor = theme1[theme]["textbox"]["insertbackground"]
	select = theme1[theme]["textbox"]["selectbackground"]
	clickedbg = theme1[theme]["button"]["clickedbg"]

	return bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, rootpath

# bg,text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = self.gettheme()


class Generator:

	def __init__(self):

		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, rootpath = gettheme()
		self.root = tkinter.Tk()
		self.root.geometry("800x600")
		self.root.configure(background=bg)

		self.root.mainloop()

def main():
	app = Generator()