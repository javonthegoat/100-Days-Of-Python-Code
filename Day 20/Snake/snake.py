from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_snake_segment(self):
        segment = Turtle()
        segment.shape("square")
        segment.penup()
        segment.color("white")
        return segment

    def create_snake(self):
        snake_head = Turtle()
        snake_head.shape("square")
        snake_head.penup()
        snake_head.color("white")
        self.segments.append(snake_head)
        for snake_segment in range(0, 2):
            segment = self.add_snake_segment()
            segment.goto(self.segments[-1].xcor() - 20, self.segments[-1].ycor()) # Position the new segment behind the last segment
            self.segments.append(segment)
    
    def down(self):
        if self.head.heading() != 90: # snake is not moving up
            self.head.setheading(270) # set the angle of the head to face down

    def right(self):
        if self.head.heading() != 180: # snake is not moving towards the left
            self.head.setheading(0) # set the angle of the head to face east

    def left(self):
        if self.head.heading() != 0: # snake is not moving towards the right
            self.head.setheading(180) # set the angle of the head to face west

    def up(self):
        if self.head.heading() != 270: # snake is not moving down
            self.head.setheading(90) # set the angle of the head to face up

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor() # Get the x-coordinate of the segment in front
            new_y = self.segments[segment - 1].ycor() # Get the y-coordinate of the segment in front
            self.segments[segment].goto(new_x, new_y) # Move the segment to the position of the segment in front
        self.head.forward(20)