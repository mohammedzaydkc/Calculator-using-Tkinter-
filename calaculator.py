import tkinter as tk
from dark_title_bar import *
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        self.root.configure(bg='#1A1A1A')
        self.root.resizable(False, False)

        # Create entry field for displaying calculations
        self.entry_field = tk.Entry(self.root, width=27,font=('Arial', 18),bg='#1A1A1A',fg='white' ,borderwidth=7)
        self.entry_field.grid(row=0, column=0, columnspan=4)

        # Create number buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.root, text=button, width=5,font=('Arial',20),bg="#1F1F1F",fg='white',command=lambda button=button: self.append_to_expression(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.root, text="C", width=5,font=('Arial',20),bg='#1F1F1F',fg='white', command=self.delete_last).grid(row=row_val, column=3, columnspan=4)
        tk.Button(self.root, text="AC", width=5,font=('Arial',20),bg='#1F1F1F' ,fg='white',command=self.clear_expression).grid(row=row_val, column=1, columnspan=4)

    def append_to_expression(self, button):
        if button == '=':
            try:
                self.expression = str(eval(self.expression))
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, self.expression)
            except Exception as e:
                self.expression = "Error"
                self.entry_field.delete(0, tk.END)
                self.entry_field.insert(tk.END, self.expression)
        else:
            self.expression += button
            self.entry_field.delete(0, tk.END)
            self.entry_field.insert(tk.END, self.expression)

    def clear_expression(self):
        self.expression = ""
        self.entry_field.delete(0, tk.END)
    def delete_last(self):
        txt=self.entry_field.get()
        self.entry_field.delete(0,tk.END)
        self.entry_field.insert(0,txt[:-1])    

if __name__ == "__main__":
    root =tk.Tk()
    dark_title_bar(root)
    calculator = Calculator(root)
    dark_title_bar(root)
    root.mainloop()
