import tkinter
import tkinter.ttk as ttk
from win32com.shell import shell, shellcon
import time
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

	return bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg

# bg,text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = self.gettheme()

class ProgressBar:

	def __init__(self, length):

		self.length = length

		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg = gettheme()

		self.window = tkinter.Tk()
		self.window.geometry("300x100")

		self.progress_var = tkinter.DoubleVar()
		self.window.bar = ttk.Progressbar(self.window, orient="horizontal", length=self.length, variable=self.progress_var, mode='determinate')
		self.window.bar.place(relx=0.5, rely=0.5, anchor="center")

		self.test_bar()

		self.window.mainloop()

	def test_bar(self):
		progress = 0
		progress_step = 1
		for i in range(self.length):
			self.window.update()
			time.sleep(1)
			progress += progress_step
			self.progress_var.set(progress)


def main():
	bar = ProgressBar(200)



if __name__ == "__main__":
	main()
