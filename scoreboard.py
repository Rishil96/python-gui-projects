from turtle import Turtle

SCOREBOARD_X = 0
SCOREBOARD_Y = 270
FONT = ("Courier", 18, "bold")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    """
    Models a scoreboard class that keeps track of the score of the current game
    """
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(SCOREBOARD_X, SCOREBOARD_Y)
        self.score = -1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
