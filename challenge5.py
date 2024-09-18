from turtle import Turtle, Screen, colormode
from random import randint, choice

# Turtle object
t1 = Turtle()
t1.shape("turtle")

# Set colormode of turtle to rgb
colormode(255)


# Function to generate random colors
def generate_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rgb = (red, green, blue)
    return rgb


# Challenge 5: Draw spirograph
t1.pendown()
t1.speed("fastest")


for angle in range(0, 361, 3):
    t1.setheading(angle)
    t1.pencolor(generate_color())
    t1.circle(150)


# Create a screen and set exit on click for the screen to not close until we click on screen
screen = Screen()
screen.exitonclick()
