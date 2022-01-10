import turtle
import random

num = random.uniform(0,3)
intNum = int(num)
print(intNum)
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Your Circle")

t = turtle.Turtle()
r = int(input("Enter the radius: "))

if intNum < 1 :
    t.fillcolor("green")
elif intNum < 2 :
    t.fillcolor("yellow")
elif intNum < 3 :
    t.fillcolor("red")
t.begin_fill()
t.circle(r)
t.end_fill()
turtle.done()
