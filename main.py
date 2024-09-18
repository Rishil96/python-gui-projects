import random

import colorgram
from turtle import Turtle, Screen, colormode

# Extract colors from image and store each color as tuple of rgb in color list
extracted_colors = colorgram.extract("spot.jpg", 25)
color_list = []

for color in extracted_colors:
    color_list.append(tuple(color.rgb))

# Copy and paste the color gram output and remove shades of white from them
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49),
              (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),
              (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229),
              (19, 21, 49), (238, 157, 216), (79, 74, 212)]


# ------------------------- Hirst painting ------------------------------
# Make a circle
def draw_circle():
    t1.color(random.choice(color_list))
    t1.dot(20, random.choice(color_list))

    # Alternative way to draw circle and fill it
    # t1.begin_fill()
    # t1.circle(10)
    # t1.end_fill()


# 10 rows and 10 columns of spots with space between each spot of size 20
start_x = -250
start_y = -250

# Turtle object
t1 = Turtle()
t1.hideturtle()

# Screen object
screen = Screen()
screen.title("Hirst Painting")

# Set speed to fastest and colormode to rgb
colormode(255)
t1.speed("fastest")
t1.penup()

# Create hirst painting
for _ in range(10):
    # Go to starting point of a new row
    t1.goto(start_x, start_y)

    # Add a circle on every column separated by 50 spaces
    for _ in range(10):
        draw_circle()
        t1.forward(50)

    # Update y-axis by 50 spaces to go to a row above
    start_y += 50

screen.exitonclick()
