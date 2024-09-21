# Pong Arcade Game
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Global variables
# Screen Config
SCREEN_TITLE = "Pong Arcade"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND_COLOR = "black"

# Initial X and Y positions of paddle
PADDLE_LEFT_X = -350
PADDLE_RIGHT_X = 350
PADDLE_Y = 0

# Pong Screen Setup
screen = Screen()
screen.title(SCREEN_TITLE)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOR)
screen.tracer(0)

# Create paddles and ball
paddle_left = Paddle(x=PADDLE_LEFT_X, y=PADDLE_Y)
paddle_right = Paddle(x=PADDLE_RIGHT_X, y=PADDLE_Y)
ball = Ball()
score = Scoreboard()

# Listen to paddle movements
screen.listen()
# Left paddle movements
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
# Right paddle movements
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

# Game logic
game_is_on = True

while game_is_on:
    # Screen animation updates every 0.1 seconds
    screen.update()

    # Keep the ball moving
    ball.move()

    # Detect collision with upper/lower wall and paddle
    ball.bounce_x(paddle_left)
    ball.bounce_x(paddle_right)
    ball.bounce_y()

    # Detect when paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_score(False)

    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_score(True)

screen.exitonclick()
