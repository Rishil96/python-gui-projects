from turtle import Turtle, Screen

# Turtle object
t1 = Turtle()
t1.shape("turtle")
t1.color("green")

# Challenge 2: Draw a dashed line
t1.pencolor("green")

for _ in range(15):
    t1.pendown()
    t1.forward(10)
    t1.penup()
    t1.forward(10)

# Create a screen and set exit on click for the screen to not close until we click on screen
screen = Screen()
screen.exitonclick()
