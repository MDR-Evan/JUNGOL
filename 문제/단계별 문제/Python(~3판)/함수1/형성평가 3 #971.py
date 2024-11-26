def square(a):
    for i in range(a):
        for j in range(a):
            print((j + 1) * (i + 1), end=' ')
        print()

num = int(input())
square(num)