# Snake Game
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Screen Borders
POSITIVE_BOUNDARY = 290
NEGATIVE_BOUNDARY = -290

# Setup Screen configurations
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Stop rendering stuff on screen till we hit update
screen.tracer(0)

# Create a snake body, food and scoreboard
snake = Snake()
food = Food()
score = ScoreBoard()

# Create listeners to control the snake movement directions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Update the screen after snake is created so creation animation is skipped to the GUI user
screen.update()

# Start game function
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food by checking if distance of head with food is less than equal to 10
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_scoreboard()

    # Detect collision with wall
    if (snake.head.xcor() > POSITIVE_BOUNDARY or snake.head.xcor() < NEGATIVE_BOUNDARY or
       snake.head.ycor() > POSITIVE_BOUNDARY or snake.head.ycor() < NEGATIVE_BOUNDARY):
        score.reset_scoreboard()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_scoreboard()
            snake.reset()

screen.exitonclick()
