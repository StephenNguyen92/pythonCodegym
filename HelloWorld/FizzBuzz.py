from posixpath import split


startNumber = int(input("Enter the start number: "))
endNumber = int(input("Enter the end number: "))

if startNumber > endNumber:
    print("Không có số phù hợp.")
else: 
    for i in range(startNumber, endNumber + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)