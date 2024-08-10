import tkinter as tk
import random
import string
from tkinter import messagebox, IntVar

def generate_password(length, complexity):
    if complexity == "weak":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation.replace("'", "")  
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation +string.ascii_uppercase
    else:
        messagebox.showwarning("Warning", "Invalid Complexity level.")
        return ''

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_and_show(length_entry, complexity_var):
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showwarning("Warning", "Password length should be a positive integer.")
            return
        
        complexity = complexity_var.get()

        password = generate_password(length, complexity)
        if password:
            password_label.config(text=f"Generated Password: {password}",bg='red',fg='white',font=('CourierNewBaltic',16))
        
    except ValueError:
        messagebox.showwarning("Invalid input", "Please enter a valid length.")
root = tk.Tk()
root.title("**Password Generator**")
length_label = tk.Label(root, text="Enter the length of the password",font=('TimesNewRoman',18))
length_label.pack(padx=10)

length_entry = tk.Entry(root, width=20)
length_entry.pack()

complexity_var = tk.StringVar()
complexity_frame = tk.Frame(root)
complexity_frame.pack(padx=10)

tk.Label(complexity_frame, text="Password Complexity").pack()

complexity_levels = [("Weak", "weak"), ("Medium", "medium"), ("Strong", "strong")]
for text, level in complexity_levels:
    tk.Radiobutton(complexity_frame, text=text, variable=complexity_var, value=level).pack(anchor=tk.W)

generate_button = tk.Button(root, text="Click to Generate Password", bg='blue',fg='white', command=lambda: generate_password_and_show(length_entry, complexity_var))
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack(pady=10)

root.mainloop()
