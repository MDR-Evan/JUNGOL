result = []

while len(result) < 100:
    num = int(input())
    if num == -1:
        break
    else:
        result.append(num)

if len(result) < 3:
    print(*result)
else:
    print(*result[-3::])