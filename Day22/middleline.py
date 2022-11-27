from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,370)
        self.color('white')
        self.width(5)
        self.drawdot()

        self.goto(0,-370)
    def drawdot(self):
        a =370
        while a !=-370:
            self.pendown()
            self.goto(0,a-10)
            a-=10
            self.penup()
            self.goto(0,a-10)
            a-=10
       


