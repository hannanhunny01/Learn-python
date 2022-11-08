import turtle as t
import random

bob = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(noSides):
    angle = 360 / noSides
    for _ in range(noSides):
        bob.forward(100)
        bob.right(angle)

for i in range(3, 10):
    bob.color(random.choice(colours))              #i = number of sides
    draw_shape(i)
    