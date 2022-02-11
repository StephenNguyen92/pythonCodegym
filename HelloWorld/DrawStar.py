import turtle

wm = turtle.Screen()
wm.bgcolor("yellow")
wm.title("My Star")

myPen = turtle.Turtle()
myPen.speed("fastest")
myPen.color("red")

for i in range(130):
    for j in range(1,6):
        myPen.forward(300)
        myPen.left(144)
    myPen.left(3)

turtle.done()