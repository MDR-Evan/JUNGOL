def max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

num1, num2, num3 = map(int, input().split())
print(max_num(num1, num2, num3))