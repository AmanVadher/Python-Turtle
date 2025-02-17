from turtle import Turtle,Screen,colormode
import random

colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color=(r,g,b)
    return color

t = Turtle()
t.speed("fastest")
t.width(2)

def draw_spirograph(gap):
    for i in range(int(360/gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading()+gap)

draw_spirograph(15)

s=Screen()
s.exitonclick()