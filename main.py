# Pong Arcade Game
from turtle import Screen
from paddle import Paddle

# Initial X and Y positions of paddle
PADDLE_LEFT_X = -350
PADDLE_RIGHT_X = 350
PADDLE_Y = 0

# Pong Screen Setup
screen = Screen()
screen.title("Pong Arcade")
screen.setup(width=800, height=600)
screen.bgcolor("black")

paddle_left = Paddle(x=PADDLE_LEFT_X, y=PADDLE_Y)
paddle_right = Paddle(x=PADDLE_RIGHT_X, y=PADDLE_Y)

# Listen to paddle movements
screen.listen()
# Left paddle movements
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
# Right paddle movements
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")

screen.exitonclick()
