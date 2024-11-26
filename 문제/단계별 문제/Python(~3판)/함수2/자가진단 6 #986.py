def bubble(num):
    for i in range(1, len(num)):
        for j in range(len(num) - i):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
        print(*num)

def select(a):
    n = len(a)
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if a[index] < a[j]:
                index = j
        a[i], a[index] = a[index], a[i]
        print(*a)

num = list(map(int,input().split()))
# bubble(num)
select(num)

