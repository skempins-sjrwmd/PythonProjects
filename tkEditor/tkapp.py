from tkinter import *

leftpane = PanedWindow()
leftpane.pack(fill=BOTH, expand=1)
sectionlist = Listbox(leftpane, selectmode=SINGLE)
leftlabel = Label(leftpane, text="left pane")
leftpane.add(leftlabel)
leftpane.add(sectionlist)

rightpane = PanedWindow(leftpane, orient=VERTICAL)
leftpane.add(rightpane)
toplabel = Label(rightpane, text="top pane")
bottomlabel = Label(rightpane, text="bottom pane")
rightpane.add(toplabel)
rightpane.add(bottomlabel)

sectionlist.insert(1, "first")
sectionlist.insert(2, "second")
sectionlist.insert(3, "third")
mainloop()