import turtle
circle = turtle.Turtle()
#đặt kích thước viền cho hình tròn là 5
circle.pensize(5)

#đặt màu sắc cho viền hình tròn là màu đỏ
circle.pencolor("blue")

#tùy chỉnh điểm bắt đầu vẽ hình tròn
turtle.Turtle().goto(-100,120)

#for outer bigger circle
#đặt màu nền cho hình tròn là màu xanh
circle.fillcolor("red")
circle.begin_fill()

#đặt bán kính hình tròn là 100
circle.circle(150)
circle.end_fill()
turtle.done()