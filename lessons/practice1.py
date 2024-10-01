import tkinter

# Window object
window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)

# GUI Components
label = tkinter.Label(text="Label 1", font=("Arial", 24, "bold"))
label.pack()


# *args to accept unlimited number of positional arguments in a function.
# args is a tuple containing all input arguments of the function
def add(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add(4, 6, 7, 8, 18, 45))
print(add(4, 6, 7, 8))
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# **kwargs to accept unlimited number of keyword arguments in a function
# kwargs is a dictionary containing all input keyword arguments of the function
def printer(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} -> {value}")


printer(rishil=28, ashwin=23, ajitha=54, ramesh=60)
printer(luffy=1, zoro=2, sanji=3, jimbei=4, robin=5)


# Button
def button_click():
    print("I got clicked!")
    # Get input from entry component
    input_val = entry.get()
    label.config(text=f"Button clicked for {input_val}!")


button = tkinter.Button(text="Click me!", command=button_click)
button.pack()


# Entry
entry = tkinter.Entry(width=15)
entry.pack()

# Keep window running
window.mainloop()
