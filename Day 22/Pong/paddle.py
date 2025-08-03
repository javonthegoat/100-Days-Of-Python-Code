from turtle import Turtle

HEIGHT = 5 # 20 * HEIGHT
MOVE = 5

class RightPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.right_paddle()

    def right_paddle(self):
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_len=HEIGHT)
        self.goto(350, 0)
        self.showturtle()

    def up(self):
        self.setpos(self.xcor(), self.ycor() + MOVE)

    def down(self):
        self.setpos(self.xcor(), self.ycor() - MOVE)

class LeftPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.left_paddle()
        
    def left_paddle(self):
        self.hideturtle()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_len=HEIGHT)
        self.goto(-350, 0)
        self.showturtle()

    def up(self):
        self.setpos(self.xcor(), self.ycor() + MOVE)

    def down(self):
        self.setpos(self.xcor(), self.ycor() - MOVE)