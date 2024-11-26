def minus(a, b):
    if a**2 > b**2:
        print(a**2 - b**2)
    else:
        print(b**2 - a**2)

num1, num2 = map(int, input().split())
minus(num1, num2)