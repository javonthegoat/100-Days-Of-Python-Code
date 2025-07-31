from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)

user_bet = screen.textinput(title="Place a bet", prompt="Which color turtle will win? Enter a color")
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-350, -100 + colors.index(color) * 30) # move each turtle to the starting line with a vertical space of 30 pixels

if user_bet:
    is_race_on = True
    while is_race_on:
        for turtle in screen.turtles():
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            if turtle.xcor() >= 350:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    screen.textinput(title="You won!", prompt=f"The {winning_color} turtle is the winner!")
                else:
                    screen.textinput(title="You lost!", prompt=f"The {winning_color} turtle is the winner!")

screen.exitonclick()