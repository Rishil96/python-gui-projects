from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.head: Turtle = Turtle()
        self.create_snake()

    def create_snake(self) -> None:
        """
        Creates the initial snake body and stores it in segments list
        """
        for position in STARTING_POSITIONS:
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)
        # Store head of snake as separate attribute for easier access
        self.head = self.segments[0]

    def move(self) -> None:
        """
        Moves the whole snake body in the direction the head is facing by 20 units
        """
        # Move each segment to its previous segment i.e. 2nd segment moves to 1st segment place
        for segment_number in range(len(self.segments)-1, 0, -1):
            next_x = self.segments[segment_number - 1].xcor()
            next_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(next_x, next_y)
        # Move head of snake forward
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        """
        Move the snake in north direction i.e. 90 degrees
        """
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self) -> None:
        """
        Move the snake in north direction i.e. 90 degrees
        """
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self) -> None:
        """
        Move the snake in north direction i.e. 90 degrees
        """
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self) -> None:
        """
        Move the snake in north direction i.e. 90 degrees
        """
        if self.head.heading() != 180:
            self.head.setheading(0)
