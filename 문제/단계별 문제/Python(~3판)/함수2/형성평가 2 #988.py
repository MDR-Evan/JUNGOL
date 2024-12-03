import math

def sqrt(a, b):
    num = 0
    a = math.sqrt(a)
    b = math.sqrt(b)

    if a <= b:
        max_ = b
        min_ = a
    else:
        max_ = a
        min_ = b

    min_ = math.ceil(min_)
    max_ = math.floor(max_)

    while min_ <= max_:
        min_ += 1
        num += 1

    print(num)

x, y = map(float, input().split())
sqrt(x, y)