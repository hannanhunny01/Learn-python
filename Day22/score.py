from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.lscore =0
        self.rscore=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,180)
        self.write(self.lscore,align='center',font=("Courier",80,'normal'))
        self.goto(100,180)
        self.write(self.rscore,align='center',font=("Courier",80,'normal'))

    def lpoint(self):
        self.lscore+=1
    def rpoint(self):
        self.rscore+=1
