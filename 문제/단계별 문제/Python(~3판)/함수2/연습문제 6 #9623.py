def sort(num):
    num.sort()
    print(*num)

num = list(map(int,input().split()))
sort(num)