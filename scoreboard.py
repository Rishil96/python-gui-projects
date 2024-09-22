from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.set_playground()

    def set_playground(self):
        """
        Draw start and finish lines on our screen
        """
        # Draw starting line
        self.pensize(width=3)
        self.goto(-280, -180)
        self.pendown()
        self.goto(260, -180)
        self.write("Start", align="right", font=FONT)

        # Draw finishing line
        self.penup()
        self.goto(-280, 200)
        self.pendown()
        self.goto(260, 200)
        self.write("Finish", align="right", font=FONT)

