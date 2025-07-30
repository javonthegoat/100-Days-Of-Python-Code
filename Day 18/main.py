from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("chocolate")

canvas = Screen()
canvas.colormode(255)  # Set color mode to RGB

def draw_square(turtle):
    for x in range(0, 4):
        turtle.forward(100)
        turtle.right(90)

def draw_dash(turtle):
    for x in range(0, 11):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()


def random_rgb():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)


def draw_shape(turtle, sides):
    angle = 360 / sides # get the angle for the shape
    for num_of_sides in range(sides):
        turtle.forward(100)
        turtle.right(angle)


def draw_shapes(turtle, shapes):
    for sides in range(3, shapes): # start from triangle (3)
        turtle.pencolor(random_rgb()) # change the pen color randomly
        draw_shape(turtle, sides)

def random_walk(turtle, distance):
    turtle.speed("fastest")  # set the turtle speed to fastest
    directions = [0, 90, 180, 270] # possible directions (east, north, west, south)
    turtle.pensize(5) # change the pen size
    turtle.setheading(random.choice(directions)) # set the turtle's direction to a random angle
    turtle.forward(distance)

def draw_spirograph(turtle, size_of_gap):
    turtle.speed("fastest")  # set the turtle's speed to fastest
    for angle in range(0, 360, size_of_gap):
        turtle.color(random_rgb())  # change the pen color to a random RGB color
        turtle.setheading(angle)  # set the turtle's heading to the current angle starting from 0 which is east
        turtle.circle(100)  # draw a circle with a radius of 100


draw_spirograph(my_turtle, 45)

canvas.exitonclick()