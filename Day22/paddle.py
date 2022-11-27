from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,xcord):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.color('white')
        self.penup()
        self.goto(xcord,0)

    def go_up(self):
        ycord = self.ycor()+20
        self.goto(self.xcor(),ycord)
    def go_down(self):
        ycord = self.ycor()-20
        self.goto(self.xcor(),ycord)
