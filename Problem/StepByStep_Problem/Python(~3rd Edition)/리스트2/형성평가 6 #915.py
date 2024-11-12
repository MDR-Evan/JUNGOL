num = map(int,input().split())
result = []

for i in num:
    if i % 2 == 0:
        result.append(int(i / 2))
    else:
        result.append(i * 2)

print(len(result))
print(*result)