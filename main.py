import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
from typing import Dict, Any

import pyperclip
import json

DEFAULT_EMAIL = "yarfik@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list.extend([choice(letters) for _ in range(randint(8, 10))])
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    input_password.delete(0, tk.END)
    input_password.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = input_website.get()
    email = input_email.get()
    pwd = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd,
        }
    }

    is_valid = len(website) > 0 and len(email) > 0 and len(pwd) > 0
    if not is_valid:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {pwd} \nIs it ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as file_data:
                    # read old data
                    data = json.load(file_data)
                    # updating
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data

            with open('data.json', 'w') as file_data:
                # saving
                json.dump(data, file_data, indent=4)

                input_website.delete(0, 'end')
                input_email.delete(0, 'end')
                input_email.insert(0, string=DEFAULT_EMAIL)
                input_password.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Manager")

lock_img = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

lbl_website = tk.Label(text="Website: ", bg="white")
lbl_website.grid(row=1, column=0)
lbl_email = tk.Label(text="Email/Username: ", bg="white")
lbl_email.grid(row=2, column=0)
lbl_password = tk.Label(text="Password: ", bg="white")
lbl_password.grid(row=3, column=0)

input_website = tk.Entry(width=51, relief="solid")
input_website.grid(row=1, column=1, columnspan=2, sticky="W")
input_website.focus()

input_email = tk.Entry(width=51, relief="solid")
input_email.grid(row=2, column=1, columnspan=2, sticky="W")
input_email.insert(tk.END, string="yarfik@gmail.com")

input_password = tk.Entry(width=32, relief="solid")
input_password.grid(row=3, column=1, sticky="W", columnspan=2)
btn_generate = tk.Button(text="Generate password", command=generate_password)
btn_generate.grid(row=3, column=2, sticky="W")

btn_add = tk.Button(text="Add", width=43, command=save)
btn_add.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()
