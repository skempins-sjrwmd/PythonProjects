import tkinter as tk

# standardize the size of widgets
STD_BUTTON_WIDTH = 6

def be_addentry_change(*args):
    if len(be_addentrystr.get()) > 0:
        be_addbutton.config(state=tk.NORMAL)
    else:
        be_addbutton.config(state=tk.DISABLED)
    be_addbutton.update_idletasks()


root = tk.Tk()
general_buttonframe = tk.LabelFrame(root, text="General")
glob_frame = tk.LabelFrame(root, text="Global Section")
def_frame = tk.LabelFrame(root, text="Defaults Section")
fe_listframe = tk.LabelFrame(root, text="Frontend Definitions")
fe_textframe = tk.LabelFrame(root)
be_listframe = tk.LabelFrame(root, text="Backend Definitions")
be_textframe = tk.LabelFrame(root)

# layout the major areas as a 3x3 gridd
general_buttonframe.grid(row=1, column=1)
glob_frame.grid(row=1, column=2)
def_frame.grid(row=1, column=3)
fe_listframe.grid(row=2, column=1)
fe_textframe.grid(row=2, column=2, columnspan=2)
be_listframe.grid(row=3, column=1)
be_textframe.grid(row=3, column=2, columnspan=2)

# add the general buttons
quit_button = tk.Button(general_buttonframe, text="Quit", command=root.destroy, width=STD_BUTTON_WIDTH)
open_button = tk.Button(general_buttonframe, text="Open", width=STD_BUTTON_WIDTH)
save_button = tk.Button(general_buttonframe, text="Save", width=STD_BUTTON_WIDTH)
quit_button.pack(side=tk.TOP, padx=5, pady=5)
open_button.pack(side=tk.TOP, padx=5, pady=5)
save_button.pack(side=tk.TOP, padx=5, pady=5)

# add the globals section area
global_applybutton = tk.Button(glob_frame, text="Apply", width=STD_BUTTON_WIDTH)
global_revertbutton = tk.Button(glob_frame, text="Revert", width=STD_BUTTON_WIDTH)
global_section_textarea = tk.Text(glob_frame, width=50, height=10)
global_section_textarea.pack(side=tk.TOP, anchor=tk.NW, padx=5)
global_applybutton.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady=5)
global_revertbutton.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady=5)

# add the defaults section area
defaults_section_textarea = tk.Text(def_frame, width=50, height=10)
defaults_applybutton = tk.Button(def_frame, text="Apply", width=STD_BUTTON_WIDTH)
defaults_revertbutton = tk.Button(def_frame, text="Revert", width=STD_BUTTON_WIDTH)
defaults_section_textarea.pack(side=tk.TOP, anchor=tk.NW, padx=5)
defaults_applybutton.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady=5)
defaults_revertbutton.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady=5)

# add the frontend areas
# create listbox and scroll
fe_listboxandscroll = tk.Frame(fe_listframe)
fe_listbox = tk.Listbox(fe_listboxandscroll, width=24, height=10)
fe_listboxscroll = tk.Scrollbar(fe_listboxandscroll, command=fe_listbox.yview, orient=tk.VERTICAL)
fe_listbox.configure(yscrollcommand=fe_listboxscroll.set)
fe_listbox.pack(side=tk.LEFT)
fe_listboxscroll.pack(side=tk.LEFT, fill=tk.Y)
# end of listbox and scroll
fe_addentryframe = tk.Frame(fe_listframe)
fe_addentry = tk.Entry(fe_addentryframe, width=18)
fe_addbutton = tk.Button(fe_addentryframe, text="Add", width=STD_BUTTON_WIDTH)
fe_addbutton.pack(side=tk.LEFT)
fe_addentry.pack(side=tk.LEFT)
fe_removebutton = tk.Button(fe_listframe, text="Remove", width=STD_BUTTON_WIDTH)

fe_listboxandscroll.pack(side=tk.TOP, padx=5, pady=5)
fe_removebutton.pack(side=tk.BOTTOM, anchor=tk.NW, padx=5, pady=5)
fe_addentryframe.pack(side=tk.BOTTOM, anchor=tk.NW, padx=5, pady=5)

#fe_cursectionname = tk.Message(fe_textframe)
fe_textarea = tk.Text(fe_textframe, width=100, height=10)
fe_applybutton = tk.Button(fe_textframe, text="Apply", width=STD_BUTTON_WIDTH)
fe_revertbutton = tk.Button(fe_textframe, text="Revert", width=STD_BUTTON_WIDTH)
#fe_cursectionname.pack(side=tk.TOP, anchor=tk.NW)
fe_textarea.pack(side=tk.TOP, anchor=tk.NW, padx=5)
fe_applybutton.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady=5)
fe_revertbutton.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady=5)

# add the backend areas
# create listbox and scroll
be_listboxandscroll = tk.Frame(be_listframe)
be_listbox = tk.Listbox(be_listboxandscroll, width=24, height=10)
be_listboxscroll = tk.Scrollbar(be_listboxandscroll, command=be_listbox.yview, orient=tk.VERTICAL)
be_listbox.configure(yscrollcommand=be_listboxscroll.set)
be_listbox.pack(side=tk.LEFT)
be_listboxscroll.pack(side=tk.LEFT, fill=tk.Y)
# end of listbox and scroll
be_addentryframe = tk.Frame(be_listframe)
be_addentrystr = tk.StringVar()
be_addentrystr.set("")
be_addentrystr.trace("w", be_addentry_change)
be_addentry = tk.Entry(be_addentryframe, textvariable=be_addentrystr, width=18)
be_addbutton = tk.Button(be_addentryframe, text="Add", width=STD_BUTTON_WIDTH, state=tk.DISABLED)
be_addbutton.pack(side=tk.LEFT, anchor=tk.NW)
be_addentry.pack(side=tk.LEFT, anchor=tk.NW)
be_removebutton = tk.Button(be_listframe, text="Remove", width=STD_BUTTON_WIDTH)

be_listboxandscroll.pack(side=tk.TOP)
be_removebutton.pack(side=tk.BOTTOM, anchor=tk.NW, padx=5, pady=5)
be_addentryframe.pack(side=tk.BOTTOM, anchor=tk.NW, padx=5, pady=5)

#be_cursectionname = tk.Message(be_textframe)
be_textarea = tk.Text(be_textframe, width=100, height=10)
be_applybutton = tk.Button(be_textframe, text="Apply", width=STD_BUTTON_WIDTH)
be_revertbutton = tk.Button(be_textframe, text="Revert", width=STD_BUTTON_WIDTH)
#be_cursectionname.pack(side=tk.TOP, anchor=tk.NW)
be_textarea.pack(side=tk.TOP, anchor=tk.NW, padx=5)
be_applybutton.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady=5)
be_revertbutton.pack(side=tk.LEFT, anchor=tk.NW, padx=5, pady=5)

fe_textframe.configure(text="Contents of section: ")
be_textframe.configure(text="Contents of section: ")
fe_addbutton.configure(state=tk.DISABLED)

root.mainloop()
