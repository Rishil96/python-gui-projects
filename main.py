# Turtle Crossing
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

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
score = Scoreboard()

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

    # Detect collision of player with car
    if car_manager.detect_collision(player=player):
        score.game_over()
        game_is_on = False

    # Check if player has crossed finish line
    if player.reached_finish_line():
        score.increase_score()
        car_manager.increase_difficulty()
        player.back_to_starting_position()

screen.exitonclick()
