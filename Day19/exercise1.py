from turtle import Turtle,Screen

bob = Turtle()

def move_f():
    bob.forward(10)

def move_b():
    bob.backward(10)

def move_l():
    bob.left(45)
    bob.forward(10)


def move_R():
    bob.right(45)
    bob.forward(10)

def clear():
    bob.clear()
    bob.penup()
    bob.home()
    bob.pendown()


screen =Screen()
screen.listen()
screen.onkey(move_f,"Up")
screen.onkey(clear,"c")
screen.onkey(move_R,"Right")
screen.onkey(move_l,"Left")
screen.onkey(move_b,"Down")

screen.exitonclick()