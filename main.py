# Turtle Race
import random
from turtle import Turtle, Screen

# Turtle Color Palette
turtle_colors = ["red", "yellow", "blue", "green", "pink", "orange"]

# Setup Screen
screen = Screen()
screen.title(titlestring="PyTurtle Racing")
screen.setup(width=600, height=400)

# Draw start and finish lines using worker turtle
worker = Turtle(shape="turtle")
worker.color("maroon")
worker.penup()

# Draw Start line
worker.goto(-210, -150)
worker.setheading(90)
worker.pendown()
worker.forward(300)
worker.penup()
worker.write("Start")

# Draw Finish line
worker.goto(230, -150)
worker.setheading(90)
worker.pendown()
worker.forward(300)
worker.penup()
worker.write("Finish")
worker.hideturtle()

# Get a guess of which turtle will win from the user
user_bet = screen.textinput(title="Make your bet",
                            prompt=f"Which turtle will win the race?\nEnter a color ({"/".join(turtle_colors)}): ")
user_bet.lower()
print(f"You have bet on the {user_bet} turtle.")

# Starting co-ordinates of each turtle
start_x = -230
start_y = -75

all_turtles = []

# Create turtle objects and place them at the start line
for i in range(len(turtle_colors)):
    # Create turtle
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[i])
    # Place turtle at start point
    new_turtle.goto(start_x, start_y)
    start_y += 30
    # Add turtle object in list
    all_turtles.append(new_turtle)

# Start the race
is_race_on = True
winner = None

while is_race_on:
    # Randomly move each turtle forward by 1-10 steps
    for turtle in all_turtles:
        steps = random.randint(1, 10)
        turtle.forward(steps)
        # Check if the current turtle reached finish line
        if turtle.xcor() >= 215:
            winner = turtle.pencolor()
            is_race_on = False

if winner == user_bet:
    print(f"You won! The '{winner}' turtle is the winner.")
else:
    print(f"You lose! The '{winner}' turtle is the winner.")

screen.exitonclick()
