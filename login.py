import tkinter as tk
from tkinter import messagebox

#function for taking input and varify the id and password.
def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_signup_form():

    print("Opening signup form...")
# Creating UI
root = tk.Tk()
root.title("Login Form")

label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_login = tk.Button(root, text="Login", command=validate_login)
btn_login.pack()

btn_signup = tk.Button(root, text="Sign Up", command=open_signup_form)
btn_signup.pack()

root.mainloop()
