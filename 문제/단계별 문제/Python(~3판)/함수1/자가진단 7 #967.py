def change(n1, n2):
    if n1 > n2:
        print("%d %d" % ((n1 // 2), (n2 * 2)))
    else:
        print("%d %d" % ((n1 * 2), (n2 // 2)))

num1, num2 = map(int, input().split())

change(num1, num2)