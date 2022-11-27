from turtle import Turtle

class Drawborder(Turtle):
    def __int__(self):
        super().__init__()
        
        self.draw()
        

    def draw(self):
        self.penup()
        self.hideturtle()
        self.goto(290,-290)
        self.hideturtle()
        self.pendown()
        self.pencolor("red")
        self.goto(290,275)
        self.goto(-290,275)
        self.goto(-290,-290)
        self.goto(290,-290)

