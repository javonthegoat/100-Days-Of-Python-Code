from turtle import Screen
from paddle import RightPaddle, LeftPaddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.listen()
screen.tracer(0)

right_paddle = RightPaddle()
left_paddle = LeftPaddle()
ping_pong_ball = Ball()
score = ScoreBoard()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ping_pong_ball.move_speed)
    
    # Detect collision with wall
    if ping_pong_ball.ycor() > 280 or ping_pong_ball.ycor() < -280:
        ping_pong_ball.bounce_y()

    # Detect collision paddle collision
    if (ping_pong_ball.xcor() > 320 and ping_pong_ball.distance(right_paddle) < 50) or  (ping_pong_ball.xcor() < -320 and ping_pong_ball.distance(left_paddle) < 50):
        ping_pong_ball.bounce_x()

    # Detect right player missed
    if ping_pong_ball.xcor() > 380:
        ping_pong_ball.reset()
        score.l_point()

    # Detect left player missed
    if ping_pong_ball.xcor() < -380:
        ping_pong_ball.reset()
        score.r_point()

    ping_pong_ball.move()