from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "bold")


class Scoreboard(Turtle):
    """
    Models a scoreboard class
    """
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Write scores on the screen
        """
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def increase_score(self, left: bool) -> None:
        """
        Based on game status, use this method to increase the score of respective players
        """
        if left:
            self.left_score += 1
        else:
            self.right_score += 1
        self.update_scoreboard()
