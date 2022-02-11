#Vòng lặp được sử dụng để lặp qua một tập hợp, một danh sách hoặc một chuỗi
# Với vòng lặp for, chúng ta có thể thực hiện một tập hợp các câu lệnh một lần cho từng mục trong danh sách hoặc chuỗi
# VÒNG LẶP FOR:
# Cú pháp:
# for val in list
# Trong đó:
# val: biến nhận giá trị của từng mục trong chuỗi trên mỗi lần lặp
# list: tập hợp các giá trị cần lặp
# statements: các dòng lệnh xử lý trong thân vòng lặp

#Lặp qua một danh sách chuỗi:
listFruit = ["apple", "banana", "orange"]
for fruit in listFruit:
    print(fruit, end=" ")
print()

#lặp qua một chuỗi:
for val in "apple":
    print(val, end=" ")
print()

#lặp qua một danh sách số
listNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in listNumber:
    print(number, end=" ")
print()

# Kết hợp với hàm range() trong vòng lặp for
# Hàm range() sẽ trả về một mảng trong đó tổng số phần tử sẽ phụ thuộc vào các tham số truyền vào
# Cú pháp: 
# range(start, end, step)
# trong đó:
# start: giá trị bắt đầu
# end: giá trị kết thúc
# step: khoảng cách giữa các phần tử, hay còn gọi là bước nhảy

#Trường hợp có một tham số:
i = 0
for i in range(5):
    print(i, end=", ")
print()

#Trường hợp có hai tham số:
for i in range(5, 10):
    print(i, end=", ")
print()

#Trường hợp có ba tham số:
for i in range(1, 10, 2):
    print(i, end=", ")
print()

#Vòng lặp for lồng nhau:
num_list = [1, 2, 3]
alpha_list = ['a', 'b', 'c']

for number in num_list:
    print(number, end = ", ")
    for letter in alpha_list:
        print(letter, end = ", " )
print()

#Một số keyword trong vòng lặp:
#Break: dừng và thoát khỏi vòng lặp
fruits = ["apple", "banana", "lemon", "melon"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break
print()

#continue: bỏ qua lần lặp một hàng hoặc các hàng cụ thể, chuyển sang bước tiếp theo
fruits = ["apple", "cherry", "melon", "banana", "lemon"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
print()

#pass: vòng lặp for không được để trống, nhưng trong trường hợp vì lý do nào đó vòng lặp không có nội dung, để tránh xảy ra lỗi, ta dùng pass
for letter in "Python":
    if letter == "h":
        pass
        print("This is pass lock")
    print("Current Letter:" ,letter)
print("Goodbye!")

#else: chỉ định 1 đoạn lệnh sẽ thực hiện khi kết thúc vòng lặp
for x in [1, 2, 3]:
    print(x)
else:
    print("Finally")

#chú ý: else sẽ không thực hiện nếu vòng lặp kết thúc bằng break
for x in [1, 2, 3, 4, 5]:
    if x == 3:
        break
    print(x)
else:
    print("for loop is done")
print("Outside the for loop")

#Sự khác nhau giữa while và for:
#Đối với vòng lặp for:
    #Câu lặp for lặp qua một tập hợp (collection), đối tượng có thể lặp (iterable object) hoặc kết quả của một hàm khởi tạo (generator function) (ví dụ range())
    #Vòng lặp for có cấu trúc đơn giản, dễ viết, là cách viết tốt nhất khi chúng ta biết số lần lặp lại.
    #Khi chúng ta có một tập hợp được tạo sẵn: a set, tuple, list, map hoặc một chuỗi văn bản thì đơn giản, chúng ta sẽ dùng vòng lặp for

#Đối với vòng lặp While:
    #Vòng lặp while là vòng lặp phụ thuộc điều kiện True or False, vòng lặp chỉ dừng lại khi điều kiện là sai
    #Vòng lặp while sử dụng khi chúng ta không biết chính xác số lần lặp qua khối lệnh
    #Nếu chúng ta không có cấu trúc dữ liệu gọn gàng để lặp lại hoặc chúng ta không có một hàm khởi tạo, bạn phải sử dụng vòng lặp while

#Ví dụ: hiển thị các số từ 1 đến 11:

#Vòng lặp for:
for i in range(12):
    print(i)

#Vòng lặp while:
num = 1
while (num < 12):
    print(num)
    num += 1
print()

#VÒNG LẶP LỒNG NHAU
#Là 1 vòng lặp xảy ra trong một vòng lặp khác, có cấu trúc tương tự câu lệnh if lồng nhau
#Ví dụ: In ra từng phần tử trong mảng lồng nhau:

list_in_list = [["hammerhead", "great white", "dogfish"],[0, 1, 2],[9.9, 8.8, 7.7]]
for list in list_in_list:
    for item in list:
        print(item)
print()