from tkinter import *

root = Tk()

t1 = Text(root)
t1.pack(side=TOP)

t2 = Text(root)
t2.pack(side=TOP)

def focusNext(widget):
	widget.tk_focusNext().focus_set()
	return 'break'

def focusPrev(widget):
	widget.tk_focusPrev().focus_set()
	return 'break'

for t in (t1, t2):
	t.bind('<Tab>', lambda e, t=t: focusNext(t))
	t.bind('<Shift-Tab>', lambda e, t=t: focusPrev(t))

t1.focus_set()

root.mainloop()
