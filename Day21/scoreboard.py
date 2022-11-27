from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
    def updatescore(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))
    def gamerover(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=("Arial",24,"normal"))