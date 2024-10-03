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
def start_timer():
    total_seconds = WORK_MIN * 60
    count_down(total_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(total_seconds):
    # Extract minutes left from total seconds and format it
    curr_minutes = total_seconds // 60
    curr_minutes = f"0{curr_minutes}" if curr_minutes <= 9 else curr_minutes

    # Extract seconds per minute left from total seconds and format it
    curr_seconds = total_seconds % 60
    curr_seconds = f"0{curr_seconds}" if curr_seconds <= 9 else curr_seconds

    # Write remaining time in minutes on the canvas
    canvas.itemconfig(timer_text, text=f"{curr_minutes}:{curr_seconds}")
    # If time still remaining, then reduce time by 1-second and call function again
    if total_seconds > 0:
        # Calls the count_down function recursively after every 1 second
        window.after(1000, count_down, total_seconds - 1)


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
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start button
start_btn = Button(text="Start", font=(FONT_NAME, 15, "bold"))
start_btn.config(borderwidth=0, command=start_timer)
start_btn.grid(row=2, column=0)

# Reset button
reset_btn = Button(text="Reset", font=(FONT_NAME, 15, "bold"))
reset_btn.config(borderwidth=0)
reset_btn.grid(row=2, column=2)

# Checkmark label
check_mark = Label(text=CHECKMARK, fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()
