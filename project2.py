import tkinter as tk
from tkinter import ttk
from math import *
import tkinter.messagebox as messagebox

class AdvancedCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Jordan's Calc")
        self.master.geometry("400x600")  # Adjusted for additional history area

        self.result_var = tk.StringVar()
        self.history_text = tk.Text(master, state='disabled', height=4, wrap='word')
        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):

        entry = ttk.Entry(self.master, textvariable=self.result_var, font=('Arial', 20), justify='right', state='readonly')
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        self.history_text.grid(row=1, column=0, columnspan=4, sticky='nsew')

        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('^', 6, 3),
            ('sqrt', 7, 0), ('log', 7, 1), ('exp', 7, 2), ('(', 7, 3),
            (')', 8, 0), ('π', 8, 1), ('e', 8, 2), ('C', 8, 3)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(self.master, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew', ipadx=10, ipady=10)

        for i in range(9):
            self.master.grid_rowconfigure(i, weight=1)
            for j in range(4):
                self.master.grid_columnconfigure(j, weight=1)

    def bind_keys(self):
        self.master.bind("<Return>", lambda event: self.on_button_click('='))
        self.master.bind("<BackSpace>", lambda event: self.on_button_click('C'))
        for key in '0123456789+-*/':
            self.master.bind(key, lambda event, key=key: self.on_button_click(key))

    def on_button_click(self, value):
        if value == '=':
            try:
                expression = self.result_var.get()
                expression = expression.replace('sin', 'sin(rad)').replace('cos', 'cos(rad)').replace('tan', 'tan(rad)').replace('^', '**').replace('sqrt', 'sqrt').replace('log', 'log').replace('exp', 'exp').replace('π', 'pi').replace('e', 'exp(1)')
                result = eval(expression)
                self.result_var.set(result)
                self.update_history(expression, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
                self.result_var.set("")
        elif value == 'C':
            self.result_var.set("")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + str(value))

    def update_history(self, expression, result):
        self.history_text.configure(state='normal')
        self.history_text.insert(tk.END, f"{expression} = {result}\n")
        self.history_text.configure(state='disabled')
        self.history_text.see(tk.END)

def main():
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
