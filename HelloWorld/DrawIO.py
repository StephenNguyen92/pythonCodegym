import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Your Shape")

t = turtle.Turtle()
t.pensize(5)
t.speed("slowest")
t.pencolor("red")
shapeInput = input("Circle and square, what is your favorite shape?:")
if shapeInput == "circle" or shapeInput == "square":
    colorInput = input("What color will it be? Red, blue or yellow?")
    if colorInput == "red" or colorInput == "blue" or colorInput == "yellow" :
        if shapeInput == "circle":
            r = int(input("Enter the radius: "))
            t.fillcolor(colorInput)
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            print("The circle with radius is {r} and color {colorInput}".format(r = r, colorInput = colorInput))

        if shapeInput == "square":
            h = int(input("Enter the side: "))
            t.fillcolor(colorInput)
            t.begin_fill()
            for i in range(4):
                t.forward(h)
                t.left(90)
            t.end_fill()
            print("The square with side is {h} and color {colorInput}".format(h = h, colorInput = colorInput))
        turtle.done()
    else: 
        print("Sorry, I don't have this color:(")
else:
    print("Sorry, I don't have this shape :(")
