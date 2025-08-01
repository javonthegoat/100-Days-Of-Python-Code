from turtle import Turtle
import random

RANGE = 290

class Food:
    def __init__(self):
        self.orb = Turtle()
        self.orb.shape("circle")
        self.orb.penup()
        self.orb.shapesize(stretch_wid=.5, stretch_len=.5)
        self.orb.color("blue")
    
    def move(self):
        random_x = random.randint(-RANGE, RANGE)
        random_y = random.randint(-RANGE, RANGE)
        self.orb.goto(random_x, random_y)