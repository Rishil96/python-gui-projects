# US States Project
import pandas as pd
import turtle

# Writer turtle
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

# Setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Add image to be used as a turtle shape
image = "blank_states_img.gif"
screen.addshape(image)

# Load states data
states = pd.read_csv("50_states.csv")

turtle.shape(image)


# Keep track of game
game_is_on = True
correct_guess_count = 0

# In game loop
while game_is_on:
    # Get state guess
    current_state = screen.textinput(title=f"{correct_guess_count}/50 States Correct",
                                     prompt="What's another state's name?")

    # Exit condition
    if current_state.lower() == "exit":
        game_is_on = False
        break

    answer = states[states["state"] == current_state.title()]
    if len(answer) == 0:
        continue
    else:
        # Get state information
        index = answer.index
        state_name = answer["state"].iloc[0]
        state_x = int(answer["x"].iloc[0])
        state_y = int(answer["y"].iloc[0])

        # Remove state from dataframe to denote it has been guessed
        states.drop(index=index, inplace=True)
        correct_guess_count += 1

        # Write state name on screen
        writer.goto(state_x, state_y)
        writer.write(f"{state_name}", font=("Courier", 8, "normal"), align="center")

# After game exit, write all missed states in a csv to return to the user
states.to_csv("missed_states.csv")

screen.mainloop()
