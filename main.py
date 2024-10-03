# Pomodoro GUI Application
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create heading label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)

# Create image using PhotoImage class and create a canvas that lets us put things on top of it
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")

# Add the image on canvas
canvas.create_image(100, 112, image=tomato_photo)
# Add text on canvas
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start button
start_btn = Button(text="Start", font=(FONT_NAME, 15, "bold"))
start_btn.config(borderwidth=0)
start_btn.grid(row=2, column=0)

# Reset button
reset_btn = Button(text="Reset", font=(FONT_NAME, 15, "bold"))
reset_btn.config(borderwidth=0)
reset_btn.grid(row=2, column=2)

# Checkmark label
check_mark = Label(text=CHECKMARK, fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()
