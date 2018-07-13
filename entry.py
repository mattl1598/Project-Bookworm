import tkinter as Tkinter
import sqlite3
import sql


class App():
	def __init__(self, text1):
		font9 = "-family {Segoe UI} -size 14 -weight normal -slant " \
				"roman -underline 0 -overstrike 0"
		self.root = Tkinter.Tk()
		self.root.geometry("200x159+700+347")
		self.root.title("Entry Form")
		self.root.configure(background="#474747")
		self.root.configure(highlightbackground="#f0f0f0f0f0f0")

		self.entry = Tkinter.Entry(self.root)
		self.entry.place(relx=0.08, rely=0.31,height=30, relwidth=0.82)

		self.button = Tkinter.Button(self.root, text = 'Submit:', command=self.quit)
		self.button.place(relx=0.28, rely=0.63, height=44, width=87)

		self.Label1 = Tkinter.Label(self.root)
		self.Label1.place(relx=0.25, rely=0.06, height=31, width=99)
		self.Label1.configure(activebackground="#474747",  activeforeground="#474747", background="#474747", disabledforeground="#a3a3a3",
							font=font9, foreground="#ffffff", text = text1)

		self.root.mainloop()

	def quit(self):
		input1 = str(self.entry.get())
		print(input1)
		sql.dbInputIn(input1)
		self.root.destroy()

#app = App()