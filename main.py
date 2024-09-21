# Pong Arcade Game
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

# Initial X and Y positions of paddle
PADDLE_LEFT_X = -350
PADDLE_RIGHT_X = 350
PADDLE_Y = 0

# Pong Screen Setup
screen = Screen()
screen.title("Pong Arcade")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Create paddles and ball
paddle_left = Paddle(x=PADDLE_LEFT_X, y=PADDLE_Y)
paddle_right = Paddle(x=PADDLE_RIGHT_X, y=PADDLE_Y)
ball = Ball()

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
    time.sleep(0.1)
    screen.update()

    # Keep the ball moving
    ball.move()

    # Detect collision with upper wall
    ball.detect_wall_collision()

screen.exitonclick()
