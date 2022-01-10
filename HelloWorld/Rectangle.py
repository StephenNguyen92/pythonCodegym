import math
import turtle

color = input("Nhập vào màu hoặc mã màu: ")
w = float(input("Nhập vào chiều dài hình chữ nhật: "))
h = float(input("Nhập vào chiều rộng hình chữ nhật: "))

t = turtle.Turtle()
t.hideturtle()

t.color(color)
t.begin_fill()
for i in range(2):
    t.forward(w)
    t.right(90)
    t.forward(h)
    t.right(90)

t.end_fill()
turtle.done()

c = 2 * (w + h)
s = w * h
print("Chu vi của hình chữ nhật có chiều dài bằng {w} và chiều rộng bằng {h} là {c}".format(w=w,h=h,c=c))
print("Diện tích của hình chữ nhật có chiều dài bằng {w} và chiều rộng bằng {h} là {s}".format(w=w,h=h,s=s))
