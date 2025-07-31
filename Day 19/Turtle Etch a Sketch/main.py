from turtle import Turtle, Screen

# Etch a Sketch program using the Turtle graphics library

jane = Turtle()
screen = Screen()

def move_forward():
    jane.forward(10)

def move_backwards():
    jane.backward(10)

def turn_left():
    jane.left(10)

def turn_right():
    jane.right(10)

def clear_screen():
    jane.clear()
    jane.penup()
    jane.home()
    jane.pendown()

screen.listen()

screen.onkey(key="space", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()