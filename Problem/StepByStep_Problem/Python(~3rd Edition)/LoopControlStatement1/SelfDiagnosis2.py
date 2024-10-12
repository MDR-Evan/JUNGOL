a = int(input())
num = 1
temp = 0

if a <= 100 :
    while num <= a:
        temp += num
        num += 1

print(temp)