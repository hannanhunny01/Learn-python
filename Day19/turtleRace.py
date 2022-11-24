from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make ur Bet",prompt="which turtle will win")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat"]

y_cordinates =[-70,-40,-10,20,50,80]

turtles =[]
for i in range(0,len(colours)):
    tim =Turtle(shape='turtle')
    tim.color(colours[i])
    tim.penup()
    tim.goto(x=-230,y=y_cordinates[i])
    turtles.append(tim)

if bet:
    start_race = True

while start_race:
    for x in turtles:
        randis = random.randint(0,10)
        if x.xcor()>240:
            start_race=False   
            winner = x.pencolor()
            if winner == bet:
                print(f"you have won!the winner is {winner}")
            else:
                print(f"You lost the winner is {winner} ")
       
        x.forward(randis)



        


screen.exitonclick()
