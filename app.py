from tkinter import *
from tkinter import ttk
import time

testVar = int(input("Test "))
choiceVar = int(input("1 or 2? "))
if choiceVar == 1:
    testVar += 1
else:
    testVar += 2

MAX = 30
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
progressbar = ttk.Progressbar(root, variable=progressVar, maximum=MAX)
def loop_function():
    k = 0
    while k <= MAX:
    ### some work to be done
        progressVar.set(k)
        k += 1
        time.sleep(0.02)
        root.update_idletasks()
    root.after(100, loop_function)
root.mainloop()