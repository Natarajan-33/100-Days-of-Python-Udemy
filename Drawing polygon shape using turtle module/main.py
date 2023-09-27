import random
from turtle import Turtle, Screen

tim=Turtle()
colors = ["red", "green", "blue", "cyan", "yellow", "magenta", "orange", "purple", "brown", "pink"]



def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for num_sides in range(3,8):
    tim.color(random.choice(colors))
    draw_shape(num_sides)



screen=Screen()
screen.exitonclick()

