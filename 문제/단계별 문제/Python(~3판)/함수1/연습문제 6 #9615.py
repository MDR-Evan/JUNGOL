def cul(a, ea, b):
    if ea == "+":
        return f"{a} + {b} = %.1f" % (a + b)
    elif ea == "-":
        return f"{a} - {b} = %.1f" % (a - b)
    elif ea == "*":
        return f"{a} * {b} = %.1f" % (a * b)
    elif ea == "/":
        return f"{a} / {b} = %.1f" % (a / b)

num1, ea, num2 = input().split()
print("%s" % cul(float(num1), ea, float(num2)))