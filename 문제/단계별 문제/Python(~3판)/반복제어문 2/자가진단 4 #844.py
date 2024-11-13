num = int(input())

if (2 <= num and num <= 100):
    for i in range(1, num+1):
        if (i % 2 == 0):
            print(i, end=' ')