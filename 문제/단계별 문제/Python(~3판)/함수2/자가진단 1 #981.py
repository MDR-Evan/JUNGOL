def R_so(a):
    a.sort(reverse=True)
    print(*a)

count = int(input())
num = list(map(int, input().split()))

R_so(num)