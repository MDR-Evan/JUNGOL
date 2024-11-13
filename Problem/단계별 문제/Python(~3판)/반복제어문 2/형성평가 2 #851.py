num1, num2 = map(int, input().split())

if num1 > num2:
    for i in range(num2, num1+1):
        print(i, end=' ')
else:
    for i in range(num1, num2+1):
        print(i, end=' ')