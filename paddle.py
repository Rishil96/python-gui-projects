from turtle import Turtle


class Paddle(Turtle):

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

    def move_up(self):
        """
        Move the paddle upwards
        """
        self.forward(20)

    def move_down(self):
        """
        Move the paddle downwards
        """
        self.backward(20)
