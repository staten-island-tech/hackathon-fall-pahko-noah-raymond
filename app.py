from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
import time


MAX = 100
root = Tk()
progressVar = DoubleVar()
frm = ttk.Frame(root, padding=400)
frm.grid()
style = ttk.Style()
style.configure("BW.TLabel", foreground="yellow", background="purple")
ttk.Label(frm, text="臭膣屄").grid(column=0, row=3)
ttk.Button(frm, text="懾屎跤", command=root.destroy).grid(column=0, row=5)
ttk.Label(frm, text="Test", style="BW.TLabel", width="100").grid(column=0, row=8)
ttk.Combobox(frm, justify="center", values=['test 1', 'test 2', 'test 3', '4', '5', '6', '7', '8', '9', '0'], state="readonly").grid(column=0, row=9)
ttk.Progressbar(frm, orient="horizontal", mode="determinate", length="1000", variable=progressVar, maximum=MAX).grid(column=0, row=15)
progressbar = ttk.Progressbar(root, variable=progressVar, maximum=MAX)
input_text = StringVar() 
  
entry1 = ttk.Entry(root, textvariable = input_text, justify = CENTER) 
entry1.focus_force() 
""" 
entry1.pack(side = TOP, ipadx = 30, ipady = 6)  """
  
save = ttk.Button(root, text = 'Save', command = lambda : askyesno( 
                                'Confirm', 'Do you want to save?')) 
###save.pack(side = TOP, pady = 10)###
def loop_function():
    k = 0
    while k <= MAX:
    ### some work to be done
        progressVar.set(k)
        k += 0.06
        time.sleep(0.01)
        root.update_idletasks()
    root.after(100, loop_function)

loop_function()
root.mainloop()