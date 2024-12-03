def area(r):
    area = r * r * 3.14
    if area % 1 >= 0.5:
        area = (area + 1)
    elif area % 1 < 0.5:
        area = area

    print("원의 넓이")
    print("버림 : %d" % (r * r * 3.14))
    print("반올림 : %d" % area)
    print("올림 : %d" % ((r * r * 3.14) + 1))

r = int(input("원의 반지름 : "))
area(r)