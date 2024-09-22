import random
from turtle import Turtle
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 5
RANDOM_Y_RANGE = (-170, 170)
START_X = 280


class Car(Turtle):
    """
    Models a single car instance
    """
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.color(random.choice(COLORS))
        random_y = random.randint(*RANDOM_Y_RANGE)
        self.goto(START_X, random_y)

    def move(self, move_speed: int):
        """
        Move car from right to left
        """
        self.forward(move_speed)


class CarManager:
    """
    Manage car spawn in game
    """
    def __init__(self):
        self.all_cars = []
        self.move_speed = 10

    def spawn_car(self) -> None:
        spawn_chance = random.randint(1, 6)
        if spawn_chance == 1:
            new_car = Car()
            self.all_cars.append(new_car)

    def move_all_cars(self) -> None:
        """
        Function to move all cars
        """
        for car in self.all_cars:
            car.move(self.move_speed)

    def detect_collision(self, player: Player) -> bool:
        """
        Check if any car has collided with the player and return true if it has
        """
        for car in self.all_cars:
            if car.distance(player) <= 25:
                return True
        return False

    def increase_difficulty(self) -> None:
        """
        Increase the speed of cars once player completes a level
        """
        self.move_speed += MOVE_INCREMENT
