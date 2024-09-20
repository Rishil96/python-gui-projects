from turtle import Turtle
from random import randint


class Food(Turtle):
    """
    Models a chunk of food to be eaten by the snake
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # By default, a turtle is 20x20, using shapesize we make it to 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Spawn the food turtle to a random location on our screen
        """
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
