import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
RANDOM_Y_RANGE = (-175, 175)
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

    def move(self):
        """
        Move car from right to left
        """
        self.forward(MOVE_INCREMENT)


class CarManager:
    """
    Manage car spawn in game
    """
    def __init__(self):
        self.all_cars = []

    def spawn_car(self):
        spawn_chance = random.randint(1, 6)
        if spawn_chance == 1:
            new_car = Car()
            self.all_cars.append(new_car)

    def move_all_cars(self):
        """
        Function to move all cars
        """
        for car in self.all_cars:
            car.move()
