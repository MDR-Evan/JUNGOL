def cal(a, b):
    while a <= b:
        print("== %ddan ==" % a)
        for i in range(9):
            print("%d * %d = %2d" % (a, i+1, (a*(i+1))))
        print()
        a += 1

def MT(a, b):
    if a < b:
        cal(a, b)
    else:
        cal(b, a)

num1, num2 = map(int, input().split())
MT(num1, num2)