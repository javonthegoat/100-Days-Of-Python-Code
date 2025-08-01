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

    def increase_score(self):
        self.score += 1

    # def update_score():
    #     self.board.write()