# Challenge 1: Build a Etch-a-Sketch app
from turtle import Turtle, Screen

t1 = Turtle()
screen = Screen()


def move_forward():
    """Function to move the turtle forward"""
    t1.forward(10)


def move_backward():
    """Function to move the turtle forward"""
    t1.backward(10)


def turn_left():
    """Function to move the turtle forward"""
    t1.left(10)


def turn_right():
    """Function to move the turtle forward"""
    t1.right(10)


def clear_screen():
    """Function to move the turtle forward"""
    t1.clear()
    t1.penup()
    t1.goto(0, 0)
    t1.setheading(0)
    t1.pendown()


# Add event listeners and listen to key events
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
