import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    password_length = int(length_entry.get())

    if password_length <= 0:
        messagebox.showerror("Error", "Password length must be a positive number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))

    user_input_label.config(text=f"User Input: {password_length}")
    generated_password_label.config(text=f"Generated Password: {generated_password}")


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:",background="AntiqueWhite",font=("Sans serif",17,"bold","italic"))
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password,width=20,background= "darkgrey",fg="black",font=(" sans Serif",15,"bold","italic"))
generate_button.pack()

user_input_label = tk.Label(root, text="USER INPUT:",background="black",fg="white",font=("Sans serif",10,"bold","italic"))
user_input_label.pack()

generated_password_label = tk.Label(root, text="Generated Password:",background="white",fg="black",font=("Sans serif",13,"bold","italic"))
generated_password_label.pack()

root.mainloop()
