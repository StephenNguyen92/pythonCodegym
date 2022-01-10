import math
import turtle

r = int(input('Enter the radius: '))
t = turtle.Turtle()
t.hideturtle()
t.pensize(1)
t.color("yellow")
t.circle(r)
turtle.done()
c = (math.pi)*2*r
s = (math.pi)*r*r
print("perimeter and acreage of the circle: {c} and {s}".format(c=c,s=s))

