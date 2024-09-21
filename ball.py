import time
from turtle import Turtle
from paddle import Paddle

BALL_MOVE_DISTANCE = 10
UPPER_WALL_LIMIT = 280
LOWER_WALL_LIMIT = -280
LEFT_WALL_LIMIT = -320
RIGHT_WALL_LIMIT = 320


SPEED_OFFSET = 0.9


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
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self) -> None:
        """
        Ball movement functionality
        """
        time.sleep(self.move_speed)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_wall_collision(self) -> bool:
        """
        Ball collision with wall implementation
        """
        # Upper wall and lower wall collision
        return self.ycor() >= UPPER_WALL_LIMIT or self.ycor() <= LOWER_WALL_LIMIT

    def bounce_y(self) -> None:
        """
        Bounce logic when ball hits upper/lower wall
        """
        # Upper/Lower wall collision bounce
        if self.detect_wall_collision():
            self.y_move *= -1

    def detect_paddle_collision(self, paddle: Paddle) -> bool:
        """
        Returns true it ball collides with paddle else false
        """
        return ((self.xcor() <= LEFT_WALL_LIMIT and self.distance(paddle) <= 50) or
                (self.xcor() >= RIGHT_WALL_LIMIT and self.distance(paddle) <= 50))

    def bounce_x(self, paddle: Paddle) -> None:
        """
        Bounce logic when ball hits a paddle
        """
        if self.detect_paddle_collision(paddle):
            self.x_move *= -1
            self.move_speed *= SPEED_OFFSET

    def reset_position(self) -> None:
        """
        When a player loses the point, ball is reset to center of the screen and game restarts
        """
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
        self.move_speed = 0.1
