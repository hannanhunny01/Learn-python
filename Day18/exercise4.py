import turtle as t
import random

bob  = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
bob.pensize(10)
random_walk = [0,90,180,270]
bob.speed(0)

for i in range(0,500):
    bob.color(random.choice(colours))
    bob.forward(30)
    bob.setheading(random.choice(random_walk))