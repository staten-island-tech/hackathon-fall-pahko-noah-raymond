from tkinter import *
from tkinter import ttk

class InputCollector:
    def __init__(self):
        self.window = Tk()
        self.entry = Entry(self.window)
        self.entry.pack()
        self.button_user_input = Button(self.window, text="Get user input", command=self.function_user_input)
        self.button_user_input.pack()
        self.button_submit = Button(self.window, text="Submit number", command=self.function_submit)
        self.button_submit.pack()
        
        self.input_values = []
        self.input_counter = 0

    def function_user_input(self):
        self.entry.delete(0, END)
        self.entry.insert(END, "Please enter your number")

    def function_submit(self):
        if self.entry.get() != "Please enter your number":
            self.input_values.append(float(self.entry.get())) # float to plotting
            self.input_counter += 1
            if self.input_counter < 3: # change this number depending on how many inputs you need
                self.function_user_input()
            else:
                self.plot_graph()

    def plot_graph(self):
        # Here is where you put your function to plot the graph
        print("Plotting graph: ", self.input_values)

    def run(self):
        self.window.mainloop()

app = InputCollector()
app.run()