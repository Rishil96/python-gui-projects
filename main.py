# Snake Game
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

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
        score.update_scoreboard()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

# TODO 3: Create snake food
# TODO 4: Detect collision with food
# TODO 5: Create a scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail


screen.exitonclick()
