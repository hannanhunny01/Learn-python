from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("yellow")
        self.speed('fastest')
        self.new_pos()
    def new_pos(self):
        postion_x = random.randint(-270,260)
        postion_y=random.randint(-270,260)
        self.goto(postion_x,postion_y)
