import turtle
import random

color = ["red", "blue", "green", "yellow", "violet"]
t = turtle.Turtle()
t.pensize(3)
t.speed("fastest")
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Vẽ Xoắn Ốc")

count = 0
while count < 2:
    t.pencolor("yellow")
    t.circle(90,90)
    t.circle(180,90)
    count += 1
turtle.done()

while count < 120:
    rColor = color[count % 5]
    t.pencolor(rColor)
    i = 0
    while i < 2:
        t.circle(180,90)
        t.circle(90,90)
        i += 1
    t.rt(3)
    count += 1
turtle.done()
