from turtle import Turtle,Screen

tur = Turtle()
tur.shape('turtle')
tur.color('green')

def move(tur):
    tur.forward(100)
    tur.left(90)
for i in range(0,4):
    move(tur)

scren = Screen()
scren.exitonclick()