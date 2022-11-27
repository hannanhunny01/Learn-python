from turtle import Turtle,Screen
from paddle import Paddle
from middleline import Line
from ball import Ball
from score import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)


paddle_left = Paddle(-350)
paddle_right =Paddle(350)
ball =Ball()
line = Line()
score = Score()


screen.listen()
screen.onkey(paddle_left.go_up,"w")
screen.onkey(paddle_left.go_down,"s")
screen.onkey(paddle_right.go_up,"Up")
screen.onkey(paddle_right.go_down,"Down")

game_one =True
while game_one:
    time.sleep(0.1)
    screen.update()
    ball.move()
 
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    
    if ball.distance(paddle_right)<50 and ball.xcor()>320 or ball.distance(paddle_left)<50 and ball.xcor()<-320 :
        ball.bounce_x()

    if ball.xcor()>380 :
        ball.reset()
        score.rpoint()
        score.update_score()
    if ball.xcor()<-380:
        ball.reset()
        score.lpoint()
        score.update_score()



        
    
screen.exitonclick()
 