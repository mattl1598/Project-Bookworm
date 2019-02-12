import tkinter
from win32com.shell import shell, shellcon
import json
import sql
import misc_python as misc

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
		self.root.geometry("300x400")
		self.root.configure(background=bg)

		self.root.loc = tkinter.Label(self.root, foreground=text, bg=bg, text="Location")

		self.school = tkinter.StringVar(self.root)
		self.lookup, self.lookup2, schools = sql.get_schools()
		self.root.loc_drop = tkinter.OptionMenu(self.root, self.school, *schools)

		self.root.loc.place(relx=1/5, rely=1/10)
		self.root.loc_drop.place(relx=2/5, rely=1/10)
		self.root.loc_drop.configure(background=button_bg, foreground=butt_txt, activebackground=clickedbg,
									activeforeground=butt_txt, highlightthickness=0, highlightcolor=bg,
									highlightbackground=bg)
		self.root.loc_drop["menu"].config(bg=button_bg, foreground=butt_txt, bd="0", activebackground="SystemHighlight",
										activeforeground=butt_txt)

		self.report = tkinter.StringVar(self.root)
		reports = misc.better_sort([])
		self.lookup, self.lookup2, schools =
		self.root.loc_drop = tkinter.OptionMenu(self.root, self.school, *reports)
		self.root.report_drop =

		self.root.mainloop()

def main():
	app = Generator()

if __name__ == "__main__":
	main()