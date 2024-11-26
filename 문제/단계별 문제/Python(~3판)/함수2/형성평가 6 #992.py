def bubble(a):
    for i in range(3):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    print(*a)

def select(a):
    n = len(a)
    for i in range(n - 1):
        index = i
        for j in range(i + 1, n):
            if a[index] > a[j]:
                index = j
        a[i], a[index] = a[index], a[i]
    print(*a)

num = list(map(int,input().split()))
bubble(num)
select(num)