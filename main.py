import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(padx=20, pady=20, bg="white")
window.title("Password Manager")

lock_img = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

lbl_website = tk.Label(text="Website: ", bg="white")
lbl_website.grid(row=1, column=0)
input_website = tk.Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)

lbl_email = tk.Label(text="Email/Username: ", bg="white")
lbl_email.grid(row=2, column=0)
input_email = tk.Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2)

lbl_password = tk.Label(text="Password: ", bg="white")
lbl_password.grid(row=3, column=0)
input_password = tk.Entry(width=21)
input_password.grid(row=3, column=1)
btn_generate = tk.Button(text="Generate Password")
btn_generate.grid(row=3, column=2)

btn_add = tk.Button(text="Add", width=36)
btn_add.grid(row=4, column=1)

window.mainloop()