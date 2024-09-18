from turtle import Turtle, Screen
from random import choice

# Turtle object
t1 = Turtle()
t1.shape("turtle")
t1.color("green")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

# Challenge 4: Draw random walk
t1.pendown()
t1.pensize(10)
t1.speed("fastest")

for _ in range(200):
    t1.pencolor(choice(colors))
    t1.setheading(choice(directions))
    t1.forward(30)


# Create a screen and set exit on click for the screen to not close until we click on screen
screen = Screen()
screen.exitonclick()
