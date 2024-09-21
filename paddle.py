from turtle import Turtle

# Constants for paddle movement limit
PADDLE_TOP_LIMIT = 250
PADDLE_BOTTOM_LIMIT = -250


class Paddle(Turtle):
    """
    Models a paddle used to play pong
    """
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        # Stretch height so it is shaped like a paddle
        self.shapesize(stretch_len=5, stretch_wid=1)
        # Go to position
        self.penup()
        self.goto(x, y)

    def move_up(self) -> None:
        """
        Move the paddle upwards
        """
        if self.ycor() < PADDLE_TOP_LIMIT:
            self.forward(20)

    def move_down(self) -> None:
        """
        Move the paddle downwards
        """
        if self.ycor() > PADDLE_BOTTOM_LIMIT:
            self.backward(20)
