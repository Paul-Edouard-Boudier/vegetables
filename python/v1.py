# ============================================================================
from tkinter import *
from tkinter import ttk

import functions as f
from gui_class import GuiVegetables
# ============================================================================
root = Tk()

# set up the main frame of the gui (if we can call it that lol)
m = ttk.Frame(root, padding="3 3 12 12")
m.grid(column=0, row=0, sticky=(N, W, E, S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)

# call our class that holds some parts of the gui, the part that we want to edit
dynamic_gui = GuiVegetables(root, m)



root.mainloop()


