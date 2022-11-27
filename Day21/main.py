from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from drawborder import Drawborder
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

food = Food()
score = ScoreBoard()
drawborder = Drawborder()
drawborder.draw()

snake = Snake()
screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")




game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food)< 15:
        food.new_pos()
        snake.increase_size()
        score.updatescore()

    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>275 or snake.segments[0].ycor()<-290:
        game_on=False
        score.gamerover()
    

    if snake.check_collison():
        game_on=False
        score.gamerover()

screen.exitonclick()