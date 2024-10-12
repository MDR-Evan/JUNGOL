num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
result = []
check = int(input())

for i in num:
    if i % check == 0:
        result.append(i)

print(result)