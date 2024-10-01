# Miles to Kilometer Converter
import tkinter

# Font Configuration
FONT = ("Arial", 12, "normal")


# Function to convert miles to km
def convert_miles_to_km():
    # Get input from entry
    miles_value = miles_entry.get()
    km_value = round(float(miles_value) * 1.609, 2)
    km_output_label.config(text=f"{km_value}")


# Create window and configurations
window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# Create entry to accept value in miles
miles_entry = tkinter.Entry(width=8)
miles_entry.config(font=FONT)
miles_entry.grid(row=0, column=1)

# Create miles label
miles_label = tkinter.Label(text="Miles")
miles_label.config(font=FONT, padx=10, pady=5)
miles_label.grid(row=0, column=2)

# equal to label
equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.config(font=FONT, padx=10, pady=5)
equal_to_label.grid(row=1, column=0)

# KM output label
km_output_label = tkinter.Label(text="0")
km_output_label.config(font=FONT, padx=10, pady=5)
km_output_label.grid(row=1, column=1)

# KM label
km_label = tkinter.Label(text="Km")
km_label.config(font=FONT, padx=10, pady=5)
km_label.grid(row=1, column=2)

# Calculate button
calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
calculate_button.config(font=FONT, padx=10, pady=5)
calculate_button.grid(row=2, column=1)

window.mainloop()
