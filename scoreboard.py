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
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER\nFINAL SCORE: {self.score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self) -> None:
        """
        Method to reset the scoreboard
        """
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = -1
        self.update_scoreboard()
