import colorgram
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
screen = Screen()
screen.colormode(255)  # Set color mode to RGB

rgb_colors = []
for color in colorgram.extract('hirt_painting.jpg', 10): # extract 10 colors from the image
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# draw dots by a set number or rows and columns and a set distance of 50 between each dot 
def draw_dots(rows, cols):
    my_turtle.penup() # pick the pen up so it doesn't draw lines
    my_turtle.hideturtle() # hide the turtle cursor
    start_x = -250
    start_y = -250
    for row in range(rows): 
        my_turtle.setpos(start_x, start_y + row * 50) # starts at the same x position and moves up by 50 pixels for each row
        for col in range(cols):
            my_turtle.dot(20, random.choice(rgb_colors)) # draw a dot with a random color from the rgb_colors list
            my_turtle.forward(50) # move forward by 50 pixels to the next dot

my_turtle.speed("fastest")  # Speed up the drawing
draw_dots(10,10)
screen.exitonclick()