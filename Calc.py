import tkinter as tk

def calculate():
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

def clear():
    entry.delete(0, tk.END)
    result.set("")

# Create the main window
root = tk.Tk()
root.title("Arithmetic Calculator")

# Variable to hold calculation result
result = tk.StringVar()

# Entry widget to input expressions
entry = tk.Entry(root, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Label to display result
result_label = tk.Label(root, textvariable=result, font=('Arial', 14), bd=5, relief=tk.RIDGE, width=30)
result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=('Arial', 14), width=5, height=2,
                       command=lambda t=text: entry.insert(tk.END, t) if t != '=' else calculate())
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text='C', font=('Arial', 14), width=5, height=2, command=clear)
clear_button.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
