from tkinter import *
from tkinter import ttk

testVar = int(input("Test "))
choiceVar = int(input("1 or 2? "))
if choiceVar == 1:
    testVar += 1
else:
    testVar += 2

root = Tk()
frm = ttk.Frame(root, padding=400)
frm.grid()
style = ttk.Style()
style.configure("BW.TLabel", foreground="yellow", background="purple")
ttk.Label(frm, text="臭膣屄").grid(column=0, row=3)
ttk.Button(frm, text="懾屎跤", command=root.destroy).grid(column=0, row=5)
ttk.Label(frm, text="Test", style="BW.TLabel", width="100").grid(column=0, row=8)
ttk.Combobox(frm, justify="center", values=['test 1', 'test 2', 'test 3', '4', '5', '6', '7', '8', '9', '0'], state="readonly").grid(column=0, row=9)
ttk.Progressbar(frm, orient="horizontal", length="500", value=testVar, mode="determinate", variable=testVar).grid(column=0, row=10)
root.mainloop()