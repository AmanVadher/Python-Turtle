from turtle import Turtle,Screen,colormode
import random

colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_tup=(r,g,b)
    return my_tup

t = Turtle()
t.speed("fastest")
t.width(10)

directions = [0,90,180,270]

for _ in range(200):
    t.color(random_color())
    t.fd(30)
    t.setheading(random.choice(directions))

s=Screen()
s.exitonclick()