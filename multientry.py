import tkinter
import json

class App():

	def gettheme(self):
		with open("D:/Project-Bookworm/theme.json", "r") as readfile:
			theme1 = json.load(readfile)

		theme = theme1["theme"]

		bg = theme1[theme]["windows"]["background"]
		text = theme1[theme]["windows"]["text"]
		buttonBG = theme1[theme]["button"]["background"]
		buttTXT = theme1[theme]["button"]["text"]
		boxBG = theme1[theme]["textbox"]["background"]
		boxTXT = theme1[theme]["textbox"]["foreground"]
		cursor = theme1[theme]["textbox"]["insertbackground"]
		select = theme1[theme]["textbox"]["selectbackground"]
		clickedbg = theme1[theme]["button"]["clickedbg"]

		return bg, text, buttonBG, buttTXT, boxBG, boxTXT, cursor, select, clickedbg
		#bg,text, buttonBG, buttTXT, boxBG, boxTXT, cursor, select, clickedbg = self.gettheme()

	def __init__(self):

		bg,text, buttonBG, buttTXT, boxBG, boxTXT, cursor, select, clickedbg = self.gettheme()

		self.root = tkinter.Tk()
		self.root.title("Test")
		self.root.geometry("1024x576")
		self.root.resizable(0,0)
		self.root.configure(background=bg)

		#scrollbar
		self.root.scrollbar = tkinter.Scrollbar(self.root)
		self.root.scrollbar.pack(side="right", fill="y")

		# note that yscrollcommand is set to a custom method for each listbox
		self.root.list1 = tkinter.Listbox(self.root, yscrollcommand=self.yscroll1)
		self.root.list1.place(x=165, y=95, width=337, height=150)
		self.root.list1.config(background=boxBG, foreground=boxTXT, bd=0)

		self.root.list2 = tkinter.Listbox(self.root, yscrollcommand=self.yscroll2)
		self.root.list2.place(x=512, y=95, width=320, height=150)
		self.root.list2.config(background=boxBG, foreground=boxTXT)

		self.root.scrollbar.config(command=self.yview)
		self.root.scrollbar.place(x=1031, y=95, height=150)

		# fill the listboxes with stuff
		for x in range(300):
			self.root.list1.insert('end', x)
			self.root.list2.insert('end', x)

		self.root.mainloop()

	def yscroll1(self, *args):     #1509860142
		if self.root.list2.yview() != self.root.list1.yview():
			self.root.list2.yview_moveto(args[0])
		self.root.scrollbar.set(*args)

	def yscroll2(self, *args):
		if self.root.list1.yview() != self.root.list2.yview():
			self.root.list1.yview_moveto(args[0])
		self.root.scrollbar.set(*args)

	def yview(self, *args):
		self.root.list1.yview(*args)
		self.root.list2.yview(*args)

def class3():
	app = App()

