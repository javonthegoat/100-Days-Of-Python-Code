from turtle import Screen
from paddle import RightPaddle

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.listen()

right_paddle = RightPaddle()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.exitonclick()
