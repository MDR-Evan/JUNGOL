def sum(a, b):
    return print("합 : %d" % (a + b))

def mul(a, b):
    return print("곱 : %d" % (a * b))

num1, num2 = map(int, input("두 수를 입력하세요. ").split())
sum(num1, num2)
mul(num1, num2)
