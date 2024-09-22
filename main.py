# Turtle Crossing
import time
from turtle import Screen
from player import Player
from car_manager import CarManager

# Screen config
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = Screen()
screen.title("PyTurtle Crossing")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

# Player turtle
player = Player()
car_manager = CarManager()

# Event listener to move turtle
screen.listen()
screen.onkey(player.move, "Up")

# Game logic
game_is_on = True

while game_is_on:
    # Update screen graphics every 0.1 second
    time.sleep(0.1)
    screen.update()

    # Randomly spawn cars based on probability and move all cars towards the left
    car_manager.spawn_car()
    car_manager.move_all_cars()

screen.exitonclick()
