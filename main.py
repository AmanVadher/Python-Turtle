import random
from turtle import Turtle,Screen,colormode
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def random_color():
    color = random.choice(color_list)
    return color

colormode(255)
t = Turtle()
t.speed("fast")
t.hideturtle()

t.setheading(225)
t.penup()
t.fd(300)
t.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    t.dot(20, random_color())
    t.penup()
    t.fd(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.fd(50)
        t.setheading(180)
        t.fd(500)
        t.setheading(0)

s = Screen()
s.exitonclick()