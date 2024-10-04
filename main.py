# Password Manager
from tkinter import *

# ------------------------------- UI SETUP ---------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Add logo on window
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Website label
website_label = Label(text="Website:", pady=5)
website_label.grid(row=1, column=0)

# Email label
email_label = Label(text="Email/Username:", pady=5)
email_label.grid(row=2, column=0)

# Password label
password_label = Label(text="Password:", pady=5)
password_label.grid(row=3, column=0)

# Website input field
website_entry = Entry(width=54)
website_entry.grid(row=1, column=1, columnspan=2)

# Email input field
email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)

# Password input field
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Generate password button
generate_button = Button(text="Generate Password", borderwidth=1)
generate_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", width=45, pady=5, borderwidth=1)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
