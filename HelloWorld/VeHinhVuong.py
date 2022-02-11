import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("square")

myPen = turtle.Turtle()
myPen.speed("slowest")
myPen.color("red")

for i in range(4):
    myPen.forward(300)
    myPen.left(90)

turtle.done()