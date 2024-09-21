from turtle import Turtle

BALL_MOVE_DISTANCE = 10
UPPER_WALL_LIMIT = 280
LOWER_WALL_LIMIT = -280


class Ball(Turtle):
    """
    Models a ball that is used to play pong
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(30)
        self.x_move = 5
        self.y_move = -10

    def move(self) -> None:
        """
        Ball movement functionality
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_wall_collision(self) -> None:
        """
        Ball collision with wall implementation
        """
        # Upper wall collision
        if self.ycor() >= UPPER_WALL_LIMIT:
            self.y_move = -self.y_move

        # Lower wall collision
        if self.ycor() <= LOWER_WALL_LIMIT:
            self.y_move = -self.y_move
