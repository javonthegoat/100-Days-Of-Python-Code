from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.listen()

paddle = Paddle()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

screen.exitonclick()
