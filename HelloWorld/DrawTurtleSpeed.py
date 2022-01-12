import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
t.hideturtle()
t.pensize(5)
turtle.bgcolor("red")
t.pencolor("yellow")
t.speed(1)
t.penup()
# Đặt vị trí ban đầu của con rùa sang bên trái
# so với vị trí giữa màn hình 400 pixel
# Mục đích để rùa chạy không ra khỏi màn hình
# khi vòng lặp quá lớn
t.goto(-400,0)
t.showturtle()

count = 0
while count < 20:
    down = random.randint(10,30)
    up = random.randint(10,30)
    t.pendown()
    t.forward(down)
    t.penup()
    t.forward(up)
    count += 1

turtle.done()