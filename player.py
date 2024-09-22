from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE = 200


class Player (Turtle):
    """
    Models the player/turtle that will cross the road
    """
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        """
        Move turtle
        """
        self.forward(MOVE_DISTANCE)
