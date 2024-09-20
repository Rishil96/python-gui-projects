# Snake Game
import time
from turtle import Screen
from snake import Snake

# Setup Screen configurations
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Stop rendering stuff on screen till we hit update
screen.tracer(0)

# Create a snake body
new_snake = Snake()

# Create listeners to control the snake movement directions
screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

# Update the screen after snake is created so creation animation is skipped to the GUI user
screen.update()

# Start game function
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()


# TODO 3: Create snake food
# TODO 4: Detect collision with food
# TODO 5: Create a scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail


screen.exitonclick()
