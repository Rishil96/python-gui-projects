from tkinter import *

window = Tk()
window.title("Challenge")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# label
label = Label(text="Label")
label.grid(row=0, column=0)

# New button
new_btn = Button(text="New Button")
new_btn.grid(row=0, column=2)

# Old button
btn = Button(text="Button")
btn.grid(row=1, column=1)

# Entry
entry = Entry()
entry.insert(END, string="Entry")
entry.grid(row=2, column=3)

window.mainloop()
