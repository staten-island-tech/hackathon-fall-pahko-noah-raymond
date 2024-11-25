from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.messagebox import askyesno 

import time

MAX = 100
root = Tk()
root.geometry('200x100') 
progressVar = DoubleVar()
style = ttk.Style()
input_text = StringVar() 
entry1 = ttk.Entry(root, textvariable = input_text, justify = CENTER) 
entry1.focus_force() 
entry1.pack(side = TOP, ipadx = 30, ipady = 6) 
  
save = ttk.Button(root, text = 'Save', command = lambda : askyesno( 
                                'Confirm', 'Do you want to save?')) 
save.pack(side = TOP, pady = 10) 
ttk.Progressbar(root, orient="horizontal", mode="determinate", length="1000", variable=progressVar, maximum=MAX)
progressbar = ttk.Progressbar(root, variable=progressVar, maximum=MAX)
progressbar.pack(side = TOP, pady = 50)

root.mainloop() 
