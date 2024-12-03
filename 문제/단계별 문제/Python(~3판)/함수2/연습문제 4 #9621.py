def area():
    area = int(input("정사각형의 넓이 : "))
    print("정사각형의 한 변의 길이 : %f" % (area ** 0.5))

def square():
    num1, num2 = map(float, input("밑과 지수 : ").split())
    print("%f의 %f승은 %f입니다." % (num1, num2, num1 ** num2))

area()
square()