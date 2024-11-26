def so(a):
    a.sort()
    print(*a)

num = list(map(int, input().split()))
so(num)