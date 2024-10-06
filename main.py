# Flash Card Learning app
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
KANJI_FONT = ("Arial", 75, "bold")
MEANING_FONT = ("Arial", 30, "bold")
FLIP_DURATION = 5000

# --------------------------- APP DATA SETUP -----------------------------------#
kanji_data = pd.read_csv("data/to_learn_kanji.csv")
to_learn = kanji_data.to_dict(orient="records")


# --------------------------- NEXT CARD LOGIC -----------------------------------#
def next_card() -> None:
    """
    This function runs when a button is clicked on screen and updates screen with a new and random kanji
    """
    # Cancels previous timers on multiple user clicks
    global flip_timer, current_card
    window.after_cancel(flip_timer)

    # Get data
    current_card = random.choice(to_learn)

    # Update canvas
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title, text="Japanese Kanji", fill="black")
    canvas.itemconfig(kanji, text=current_card.get("Kanji"), font=KANJI_FONT)
    canvas.itemconfig(english_meaning, text="")
    canvas.itemconfig(onyomi, text=f"Onyomi: {current_card.get("Onyomi")}")
    canvas.itemconfig(kunyomi, text=f"Kunyomi: {current_card.get("Kunyomi")}")

    # Flip card after 5 seconds
    flip_timer = window.after(FLIP_DURATION, flip_card, current_card)


def flip_card(kanji_card: dict):
    """
    This function flips the card which is the answer to the question
    """
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English Meaning", fill="white")
    canvas.itemconfig(english_meaning, text=f"{kanji_card["Kanji Meaning"]}", fill="white")
    canvas.itemconfig(kanji, text="")
    canvas.itemconfig(onyomi, text="")
    canvas.itemconfig(kunyomi, text="")


def is_known():
    """
    Function to remove kanji from to learn csv
    """
    global current_card
    # Update learning material by removing learned kanji
    to_learn.remove(current_card)
    updated_to_learn_data = pd.DataFrame(to_learn)
    updated_to_learn_data.to_csv("data/to_learn_kanji.csv", index=False)
    next_card()


# --------------------------- UI SETUP -----------------------------------#

window = Tk()
window.title("Kanji Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Timer and card variable
current_card = {}
flip_timer = "after#0"

# Add card image using canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Add kanji texts on top of our canvas
title = canvas.create_text(400, 100, text="Japanese Kanji", font=("Arial", 25, "italic"))
kanji = canvas.create_text(400, 200, text="&", font=("Arial", 75, "bold"))
english_meaning = canvas.create_text(400, 250, text="", font=MEANING_FONT, width=500)
onyomi = canvas.create_text(400, 320, text="Onyomi:", font=("Arial", 20, "italic"), width=600)
kunyomi = canvas.create_text(400, 380, text="Kunyomi:", font=("Arial", 20, "italic"), width=600)

canvas.grid(row=0, column=0, columnspan=2)

# Add correct and incorrect buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
