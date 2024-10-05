# Password Manager
import random
import pyperclip
import json
from tkinter import *
from tkinter import messagebox


# ------------------------------- SEARCH DATA ---------------------------------- #
def search_data():

    # Read website name to search for it
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="ERROR", message="Please type the name of the website first!")
        return

    # Open the data file
    try:
        with open("data.json", "r") as json_file:
            password_db = json.load(json_file)

    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="No password database found, try adding some passwords first")

    else:
        try:
            display_data = password_db[website]
        except KeyError:
            messagebox.showerror(title="404", message=f"Password not found for {website}")
        else:
            messagebox.showinfo(title=website, message=f"Email/Username: {password_db[website]["email"]}\n"
                                                       f"Password: {password_db[website]["password"]}")


# ------------------------------- PASSWORD GENERATOR ---------------------------------- #
def generate_password():
    # Python Password Generator
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+',
               '=', '[', ']', '{', '}', '|', ';', ':', '<', '>', '/', '?', '~']

    letter_count = random.randint(10, 12)
    symbol_count = random.randint(3, 5)
    number_count = random.randint(3, 5)

    password_list = []

    # Get random letters
    letters_list = [random.choice(letters) for _ in range(0, letter_count)]

    # Get random numbers
    numbers_list = [random.choice(numbers) for _ in range(0, number_count)]

    # Get random symbols
    symbols_list = [random.choice(symbols) for _ in range(0, symbol_count)]

    # Add letters, numbers, and symbols in password list
    password_list.extend(letters_list)
    password_list.extend(numbers_list)
    password_list.extend(symbols_list)

    # Shuffle password characters
    random.shuffle(password_list)

    # Insert generated password on UI
    password = ''.join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(index=0, string=password)

    # Copy password in our clipboard
    pyperclip.copy(password)

    return


# ------------------------------- SAVE DATA ---------------------------------- #
def save_data():
    # Get website, email and password entry
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()

    if len(website_input) == 0 or len(email_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title="OOPS!", message="Please don't leave any fields empty!")
        return

    # Popup box for user confirmation
    is_ok = messagebox.askokcancel(title=website_input, message="Here are the details of your password:-\n"
                                                                f"Username/Email: {email_input}\n"
                                                                f"Password: {password_input}\n"
                                                                f"Do you want to go ahead and save this?")

    # Write data in JSON format
    password_data = {
        website_input: {
            "email": email_input,
            "password": password_input,
        }
    }

    if is_ok:
        try:
            # Read JSON data and update it with new data in code
            with open("data.json", "r") as json_file:
                # Read JSON data
                full_data = json.load(json_file)

        except FileNotFoundError:
            print("No database found. Creating a new one...")
            with open("data.json", "w") as json_file:
                json.dump(password_data, json_file, indent=4)

        else:
            full_data.update(password_data)
            # Write updated JSON back to the file
            with open("data.json", "w") as json_file:
                json.dump(full_data, json_file, indent=4)

        finally:
            print("Data added successfully!")
            # Clear entry data
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            # Info popup
            messagebox.showinfo(title=website_input, message="Password was saved successfully!")
    else:
        # Info popup
        messagebox.showinfo(title=website_input, message="Password was not saved.")

    # Bring focus back to first entry
    website_entry.focus()

    return


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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

# Email input field
email_entry = Entry(width=54)
email_entry.grid(row=2, column=1, columnspan=2)

# Password input field
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Generate password button
generate_button = Button(text="Generate Password", borderwidth=1, command=generate_password)
generate_button.grid(row=3, column=2)

# Add button
add_button = Button(text="Add", width=45, pady=5, borderwidth=1, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

# Search button
search_button = Button(text="Search", borderwidth=1, width=14, command=search_data)
search_button.grid(row=1, column=2)

window.mainloop()
