import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("400x600")  # Set the window size to be wider
        self.root.resizable(0, 0)  # Prevent resizing

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

        self.buttons_frame.rowconfigure(0, weight=1)
        for i in range(1, 5):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg="lightgray", fg="black", padx=24, font=("Arial", 18))
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="lightgray", fg="black", padx=24, font=("Arial", 40, "bold"))
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg="lightgray")
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root, bg="gray")
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="white", fg="black", font=("Arial", 24, "bold"), borderwidth=1, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW, padx=1, pady=1)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="#FFA07A", fg="black", font=("Arial", 24, "bold"), borderwidth=1, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW, padx=1, pady=1)
            i += 1

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="#FF6347", fg="black", font=("Arial", 24, "bold"), borderwidth=1, command=self.clear)
        button.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW, padx=1, pady=1)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="#98FB98", fg="black", font=("Arial", 24, "bold"), borderwidth=1, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW, padx=1, pady=1)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x²", bg="#FFA07A", fg="black", font=("Arial", 24, "bold"), borderwidth=1, command=self.square)
        button.grid(row=0, column=3, sticky=tk.NSEW, padx=1, pady=1)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="√", bg="#FFA07A", fg="black", font=("Arial", 24, "bold"), borderwidth=1, command=self.sqrt)
        button.grid(row=0, column=4, sticky=tk.NSEW, padx=1, pady=1)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    @property
    def digits(self):
        return {
            7: (1, 0), 8: (1, 1), 9: (1, 2),
            4: (2, 0), 5: (2, 1), 6: (2, 2),
            1: (3, 0), 2: (3, 1), 3: (3, 2),
            0: (4, 0), '.': (4, 1)
        }

    @property
    def operations(self):
        return {
            "/": "÷", "*": "×", "-": "-", "+": "+"
        }

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
