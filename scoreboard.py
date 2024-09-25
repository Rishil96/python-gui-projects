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
        self.high_score = self.read_high_score()
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
            self.write_high_score(self.high_score)

        self.score = -1
        self.update_scoreboard()

    @staticmethod
    def read_high_score() -> int:
        """
        Read high score from data file and return it
        """
        with open(file="data.txt", mode="r") as file:
            high_score = file.read()
            high_score = int(high_score)
        return high_score

    @staticmethod
    def write_high_score(high_score: int) -> None:
        """
        Write new high score in data file
        """
        with open(file="data.txt", mode="w") as file:
            file.write(str(high_score))
