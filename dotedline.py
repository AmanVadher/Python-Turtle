from turtle import Turtle, Screen
t = Turtle()

for i in range(10):
    t.fd(10)
    t.penup()
    t.fd(10)
    t.pendown()

s = Screen()
s.exitonclick()