def cal(a, ea, b):
    if ea == "+":
        return f"{a} + {b} = {a + b}"
    elif ea == "-":
        return f"{a} - {b} = {a - b}"
    elif ea == "*":
        return f"{a} * {b} = {a * b}"
    elif ea == "/":
        return f"{a} / {b} = {a // b}"

num1, ea, num2 = input().split()
print(cal(int(num1), ea, int(num2)))