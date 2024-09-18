from turtle import Turtle, Screen

# Turtle object
t1 = Turtle()
t1.shape("turtle")
t1.color("green")

# Challenge 1: Draw a square
t1.pencolor("green")
t1.pendown()

for _ in range(4):
    t1.forward(100)
    t1.right(90)

# Create a screen and set exit on click for the screen to not close until we click on screen
screen = Screen()
screen.exitonclick()
