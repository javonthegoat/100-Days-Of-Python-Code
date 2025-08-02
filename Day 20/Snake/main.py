from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off the screen updates for performance

snake = Snake()
food = Food()
food.move()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
game_over = False


while game_is_on:
    screen.update()
    time.sleep(0.1)  # Control the speed of the game

    if not game_over:
        snake.move()

    # Check if snake ate food if it did move the food, increase the score, and add a segment to the snake
    if snake.head.distance(food.orb.position()) < 15:
        food.move() # move the food randomly within the screen bounds
        score.update_score() # increase the score
        snake.segments.append(snake.add_snake_segment()) # add a segment to the snake

    # Check if the snakes head collided with its own body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment.position()) <= 19:
            game_over = True
            score.game_over()
            print("Game Over! You slithered into your own body.")

    # Check for collision with the wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_over = True
        score.game_over()
        print("Game Over! You hit the wall.")