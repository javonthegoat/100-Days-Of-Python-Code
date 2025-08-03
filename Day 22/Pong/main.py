from turtle import Screen
from paddle import RightPaddle, LeftPaddle

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.listen()
screen.tracer(0)

right_paddle = RightPaddle()
left_paddle = LeftPaddle()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()