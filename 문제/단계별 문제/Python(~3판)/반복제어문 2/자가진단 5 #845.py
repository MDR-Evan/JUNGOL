num = int(input())
sum = 0

if num <= 100:
    for i in range(num, 101):
        sum += i

    print(sum)