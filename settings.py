<<<<<<< HEAD
import tkinter
import homepage
import json


def gettheme():
	# get colours from json file
	with open("D:/Project-Bookworm/theme.json", "r") as readfile:
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

	return bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, theme


class Options:

	def __init__(self):

		# import colours
		bg, text, button_bg, butt_txt, box_bg, box_txt, cursor, select, clickedbg, current_theme = gettheme()

		self.setts = tkinter.Tk()
		self.setts.title("Settings")
		self.setts.configure(background=bg)

		themes = [
			"dark",
			"light",
			"custom"
		]

		self.theme = tkinter.StringVar(self.setts)
		self.theme.set(current_theme)

		# option menu setup and config
		self.themeDrop = tkinter.OptionMenu(self.setts, self.theme, *themes)
		self.themeDrop.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
									activeforeground=butt_txt, highlightthickness=0, highlightcolor=bg, highlightbackground=bg)
		self.themeDrop["menu"].config(bg=button_bg, foreground=butt_txt, bd="0", activebackground="SystemHighlight",
										activeforeground=butt_txt)
		print(self.themeDrop)
		self.themeDrop.pack()

		self.quit = tkinter.Button(text="Close", command=lambda: self.close(current_theme))
		self.quit.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg, activeforeground=butt_txt)
		self.quit.pack()

		self.setts.mainloop()

	def apply(self, current_theme):
		theme = self.theme.get()

		if theme != current_theme:

			with open("D:/Project-Bookworm/theme.json", "r") as file:
				# doesnt work as one line. has to be two seperate "with opens" to modify a json.
				theme1 = json.load(file)

			theme1["theme"] = theme

			with open("D:/Project-Bookworm/theme.json", "w") as file:
				json.dump(theme1, file, indent=4)

	def close(self, current_theme):
		self.apply(current_theme)
		self.setts.destroy()
		homepage.main()


def main():
	window = Options()
=======
import tkinter
import homepage
import json

class options():

	def gettheme(self):

		#get colours from json file
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

		return bg, text, buttonBG, buttTXT, boxBG, boxTXT, cursor, select, clickedbg, theme

	def __init__(self):


		#import colours
		bg, text, buttonBG, buttTXT, boxBG, boxTXT, cursor, select, clickedbg, currentTheme = self.gettheme()
		self.setts = tkinter.Tk()
		self.setts.title("Settings")
		self.setts.configure(background=bg)

		themes = [
			"dark",
			"light",
			"custom"
		]

		self.theme = tkinter.StringVar(self.setts)
		self.theme.set(currentTheme)


		#option menu setup and config
		self.themeDrop = tkinter.OptionMenu(self.setts, self.theme, *themes)
		self.themeDrop.configure(background=buttonBG, foreground=buttTXT, activebackground=clickedbg, activeforeground=buttTXT, highlightthickness=0, highlightcolor=bg, highlightbackground=bg)
		self.themeDrop["menu"].config(bg=buttonBG, foreground=buttTXT, bd="0", activebackground="SystemHighlight", activeforeground=buttTXT)
		print(self.themeDrop)
		self.themeDrop.pack()

		self.quit = tkinter.Button(text="Close", command= lambda: self.close(currentTheme))
		self.quit.configure(background=buttonBG, foreground=buttTXT, activebackground=clickedbg, activeforeground=buttTXT)
		self.quit.pack()

		self.setts.mainloop()

	def apply(self, currentTheme):
		theme = self.theme.get()

		if theme != currentTheme:

			with open("D:/Project-Bookworm/theme.json", "r") as file:  # doesnt work as one line. has to be two seperate "with opens" to modify a json.
				theme1 = json.load(file)

			theme1["theme"] = theme

			with open ("D:/Project-Bookworm/theme.json", "w") as file:
				json.dump(theme1, file, indent=4)



	def close(self, currentTheme):
		self.apply(currentTheme)
		self.setts.destroy()
		homepage.main()

def main():
	window = options()
>>>>>>> 77d70087116cb3542db994ff5dd771921a03de6f
