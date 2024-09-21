from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 70, "bold")
WINNING_SCORE = 1


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
        self.winner = ""

    def update_scoreboard(self) -> None:
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

    def game_over(self) -> bool:
        """
        Check is a player has won
        """
        if self.left_score == WINNING_SCORE:
            self.winner = "left"
            return True
        elif self.right_score == WINNING_SCORE:
            self.winner = "right"
            return True
        else:
            return False

    def display_final_result(self) -> None:
        """
        Display final result after game is over
        """
        self.clear()
        self.goto(0, 0)
        self.write(f"\t   GAME OVER\n"
                   f"{self.winner.title()} player won the game by {self.left_score}-{self.right_score}",
                   align=ALIGNMENT,
                   font=("Courier", 20, "bold"))
