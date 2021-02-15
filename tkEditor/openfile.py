# importing tkinter and tkinter.ttk
# and all their functions and classes
import tkinter as tk
import tkinter.filedialog

#from tkinter.ttk import *

# importing askopenfile function
# from class filedialog
#from tkinter.filedialog import askopenfile

root = tk.Tk()
root.geometry('200x100')

# This function will be used to open
# file in read mode and only Python files
# will be opened
def open_file():
    file = tk.filedialog.askopenfile(mode='r')
    if file is not None:
        content = file.read()
        print(content)


btn = tk.Button(root, text='Open', command=lambda: open_file())
btn.pack(side=tk.TOP, pady=10)

root.mainloop()
