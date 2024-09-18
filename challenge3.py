from turtle import Turtle, Screen
from random import choice

# Turtle object
t1 = Turtle()
t1.shape("turtle")
t1.color("green")

colors = ["green", "blue", "yellow", "red", "orange", "pink", "purple", "brown", "grey", "black"]

# Challenge 3: Draw shapes from triangle to decagon
t1.pendown()

for side in range(3, 11):
    t1.pencolor(choice(colors))
    angle = 360 / side
    for _ in range(side):
        t1.forward(100)
        t1.right(angle)


# Create a screen and set exit on click for the screen to not close until we click on screen
screen = Screen()
screen.exitonclick()
