# tk.button(myForm, text="+", btnPressed="+", command = lambda t="+":calculated(t))
# =lambda t= "Button-1 Clicked": get_button(t)
#pack()    
#USE OF LAMBDA FUNCTION


import tkinter as tk
from tkinter import messagebox

# Function for taking input and performing arithmetic operations
def calculate(operation):
    try:
        number1 = float(entry_username.get())
        number2 = float(entry_password.get())
        if operation == "Addition":
            output = number1 + number2
        elif operation == "Substraction":
            output = number1 - number2
        elif operation == "Multiplication":
            output = number1 * number2
        elif operation == "Division":
            output = number1 / number2
        messagebox.showinfo("Result", f"Result: {output}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Creating UI
root = tk.Tk()
root.title("Calculator")

label_username = tk.Label(root, text="1st Number")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="2nd Number")
label_password.pack()
entry_password = tk.Entry(root)
entry_password.pack()

# Added buttons for arithmetic operations
btn_Add = tk.Button(root, text="Addition", command=lambda: calculate("Addition"))
btn_Add.pack()

btn_Sub = tk.Button(root, text="Substraction", command=lambda: calculate("Substraction"))
btn_Sub.pack()

btn_Mul = tk.Button(root, text="Multiplication", command=lambda: calculate("Multiplication"))
btn_Mul.pack()

btn_Div = tk.Button(root, text="Division", command=lambda: calculate("Division"))
btn_Div.pack()

root.mainloop()

