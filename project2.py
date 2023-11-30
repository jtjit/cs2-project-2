import tkinter as tk
from tkinter import ttk
from math import *

class AdvancedCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Calculator")
        self.master.geometry("400x500")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Entry for displaying the result
        entry = ttk.Entry(self.master, textvariable=self.result_var, font=('Arial', 20), justify='right')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('^', 5, 3),
            ('sqrt', 6, 0), ('log', 6, 1), ('exp', 6, 2), ('(', 6, 3),
            (')', 7, 0), ('π', 7, 1), ('e', 7, 2), ('C', 7, 3)
        ]

        # Create buttons
        for (text, row, col) in buttons:
            button = ttk.Button(self.master, text=text, command=lambda t=text: self.on_button_click(t),
                                style="TButton" if text.isdigit() or text in ['.', '=', 'C'] else "Operator.TButton")
            button.grid(row=row, column=col, sticky='nsew', ipadx=10, ipady=10)

        # Configure row and column weights
        for i in range(8):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, value):
        if value == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif value == 'C':
            self.result_var.set("")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + str(value))

def main():
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
