from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Models a snake that is created on Screen from turtle module
    """
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        """
        Creates the initial snake body and stores it in segments list
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position) -> None:
        """
        Add a new segment to the snake body
        """
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.segments.append(segment)

    def extend(self) -> None:
        """
        Extend when the snake eats food
        """
        self.add_segment(position=self.segments[-1].position())

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
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """
        Move the snake in north direction i.e. 90 degrees
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """
        Move the snake in north direction i.e. 90 degrees
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """
        Move the snake in north direction i.e. 90 degrees
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
