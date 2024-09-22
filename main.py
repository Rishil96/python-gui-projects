# Turtle Crossing
import time
from turtle import Screen

# Screen config
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.title("PyTurtle Crossing")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()


screen.exitonclick()
