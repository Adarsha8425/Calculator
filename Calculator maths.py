import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.config(bg="#222831")
        self.expression = ""
        self.memory = 0

        # Entry field
        self.entry = tk.Entry(root, font=('Arial', 30), bg="#ffffff", fg="#000000",
                              borderwidth=5, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=6, ipadx=8, ipady=15, padx=10, pady=10)

        self.create_buttons()

    def click(self, value):
        self.expression += str(value)
        self.update_display()

    def clear(self):
        self.expression = ""
        self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.expression.replace("^", "**")))
            self.expression = result
            self.update_display()
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
            self.expression = ""

    def update_display(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def scientific_func(self, func):
        try:
            value = eval(self.expression)
            result = ""
            if func == "sin":
                result = str(math.sin(math.radians(value)))
            elif func == "cos":
                result = str(math.cos(math.radians(value)))
            elif func == "tan":
                result = str(math.tan(math.radians(value)))
            elif func == "log":
                result = str(math.log10(value))
            elif func == "sqrt":
                result = str(math.sqrt(value))
            self.expression = result
            self.update_display()
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")
            self.expression = ""

    def memory_func(self, cmd):
        try:
            if cmd == "MC":
                self.memory = 0
            elif cmd == "M+":
                self.memory += eval(self.expression)
            elif cmd == "M-":
                self.memory -= eval(self.expression)
            elif cmd == "MR":
                self.expression = str(self.memory)
                self.update_display()
        except:
            self.expression = ""
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

    def create_buttons(self):
        button_cfg = {'font': ('Arial', 14), 'width': 5, 'height': 2, 'bg': '#393E46', 'fg': 'white'}
        sci_button_cfg = {'font': ('Arial', 14), 'width': 5, 'height': 2, 'bg': '#00ADB5', 'fg': 'white'}
        mem_button_cfg = {'font': ('Arial', 14), 'width': 5, 'height': 2, 'bg': '#FF5722', 'fg': 'white'}

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4), ('MC', 1, 5),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4), ('M+', 2, 5),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4), ('M-', 3, 5),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3), ('log', 4, 4), ('MR', 4, 5),
            ('^', 5, 0), ('(', 5, 1), (')', 5, 2), ('sqrt', 5, 3), ('=', 5, 4, 2)
        ]

        for item in buttons:
            text, row, col = item[0], item[1], item[2]
            colspan = item[3] if len(item) == 4 else 1

            if text in ('sin', 'cos', 'tan', 'log', 'sqrt'):
                cmd = lambda t=text: self.scientific_func(t)
                cfg = sci_button_cfg
            elif text in ('MC', 'M+', 'M-', 'MR'):
                cmd = lambda t=text: self.memory_func(t)
                cfg = mem_button_cfg
            elif text == 'C':
                cmd = self.clear
                cfg = button_cfg
            elif text == '=':
                cmd = self.calculate
                cfg = {'font': ('Arial', 14), 'width': 12, 'height': 2, 'bg': '#6ab04c', 'fg': 'white'}
            else:
                cmd = lambda t=text: self.click(t)
                cfg = button_cfg

            btn = tk.Button(self.root, text=text, command=cmd, **cfg)
            btn.grid(row=row, column=col, columnspan=colspan, padx=4, pady=4)


# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
