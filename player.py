from turtle import Turtle

STARTING_POSITION = (0, -220)
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

    def move(self) -> None:
        """
        Move turtle
        """
        self.forward(MOVE_DISTANCE)

    def reached_finish_line(self) -> bool:
        """
        Returns true if player has crossed the finish line
        """
        return self.ycor() >= FINISH_LINE

    def back_to_starting_position(self) -> None:
        """
        Bring player back to starting line
        """
        self.goto(STARTING_POSITION)
