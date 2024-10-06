# Flash Card Learning app
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------- APP DATA SETUP -----------------------------------#
kanji_data = pd.read_csv("data/kanji.csv")


def get_random_kanji() -> pd.Series:
    """
    This function returns a random kanji from the kanji data
    """
    data_length = len(kanji_data)
    random_index = random.randint(0, data_length - 1)
    random_kanji = kanji_data.iloc[random_index, :]

    return random_kanji


def update_canvas() -> None:
    """
    This function runs when a button is clicked on screen and updates screen with a new and random kanji
    """
    # Get data
    random_kanji = get_random_kanji()
    kanji_character = random_kanji.Kanji
    onyomi_info = random_kanji.Onyomi
    kunyomi_info = random_kanji.Kunyomi
    # Update canvas
    canvas.itemconfig(kanji, text=kanji_character)
    canvas.itemconfig(onyomi, text=f"Onyomi: {onyomi_info}")
    canvas.itemconfig(kunyomi, text=f"Kunyomi: {kunyomi_info}")


# --------------------------- UI SETUP -----------------------------------#

window = Tk()
window.title("Kanji Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Add card image using canvas
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Add kanji texts on top of our canvas
title = canvas.create_text(400, 100, text="Japanese Kanji", font=("Arial", 25, "italic"))
kanji = canvas.create_text(400, 200, text="&", font=("Arial", 75, "bold"))
onyomi = canvas.create_text(400, 320, text="Onyomi:", font=("Arial", 20, "italic"), width=600)
kunyomi = canvas.create_text(400, 380, text="Kunyomi:", font=("Arial", 20, "italic"), width=600)

canvas.grid(row=0, column=0, columnspan=2)

# Add correct and incorrect buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=update_canvas)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=update_canvas)
wrong_button.grid(row=1, column=1)

update_canvas()


window.mainloop()
