from turtle import Turtle

class ScoreBoard:

    def __init__(self):
        self.score = 0
        self.board = Turtle()
        self.board.color("white")
        self.board.penup()
        self.board.goto(0, 280)
        self.board.write(arg=f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))
        self.board.hideturtle()

    def game_over(self):
        self.board.home()
        self.board.write(arg="GAME OVER", align="center", font=("Arial", 12, "normal"))

    def update_score(self):
        self.board.clear() # get rid of the previous score
        self.score += 1
        self.board.write(arg=f"Score: {self.score}", align="center", font=("Arial", 12, "normal"))