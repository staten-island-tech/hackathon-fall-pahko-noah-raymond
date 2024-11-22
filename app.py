from tkinter import *
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
entry= Entry(frm).grid(column=1,row=78)
entry.focus_set()
entry.pack()
ttk.Button(frm, text= "Okay", command= display_text).grid(column=1,row=1909909990)
def loop_function():
    k = 0
    while k <= MAX:
    ### some work to be done
        progressVar.set(k)
        k += 0.2
        time.sleep(0.01)
        root.update_idletasks()
    root.after(100, loop_function)

loop_function()
root.mainloop()