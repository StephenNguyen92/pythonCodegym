import turtle

a = int(input("Nhập vào độ dài 1 cạnh hình vuông: "))

t = turtle.Turtle()
t.hideturtle()
t.pensize(5)
t.pencolor("red")
t.fillcolor("yellow")
t.speed("slowest")
t.begin_fill()

side = 0
while side < 4:
    t.forward(a)
    t.left(90)
    side += 1

t.end_fill()
turtle.done()
