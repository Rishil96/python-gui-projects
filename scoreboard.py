from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGNMENT = "right"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def set_playground(self) -> None:
        """
        Draw start and finish lines on our screen
        """
        # Draw starting line
        self.pensize(width=3)
        self.goto(-280, -180)
        self.pendown()
        self.goto(260, -180)
        self.write("Start", align=ALIGNMENT, font=FONT)

        # Draw finishing line
        self.penup()
        self.goto(-280, 200)
        self.pendown()
        self.goto(260, 200)
        self.write("Finish", align=ALIGNMENT, font=FONT)
        self.penup()

    def update_scoreboard(self) -> None:
        """
        Update scoreboard
        """
        self.clear()
        self.set_playground()
        self.goto(-150, 250)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def increase_score(self) -> None:
        """
        Function to increase score of player
        """
        self.level += 1
        self.update_scoreboard()

    def game_over(self) -> None:
        """
        Display game over message
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
