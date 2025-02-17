from turtle import Turtle,Screen
import random

t = Turtle()
color=["blue","dark green","dark red","dark goldenrod","dark olive green","deep pink","indigo"]

def draw_shape(side):
    angle = 360 / side
    for _ in range(side):
        
        t.fd(100)
        t.lt(angle)

for i in range(3,11):
    t.color(random.choice(color))
    draw_shape(i)

s = Screen()
s.exitonclick()