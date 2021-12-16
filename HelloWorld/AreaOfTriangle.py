import math

#Nhập dữ liệu từ bàn phím và lưu vào 3 biến a,b,c
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

#Tính diện tích tam giác theo công thức area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#Trong đó s là chu vi của tam giác, được tính với công thức: “s = (a+b+c)/2”
#math.sqrt là hàm tính căn bậc hai

s = (a + b + c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

#In ra kết quả
print("Area of the triangle is: ", area)
