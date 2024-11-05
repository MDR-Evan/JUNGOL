num = list(map(int,input().split()))
min_result = []
max_result = []

for i in num:
    if i < 100:
        max_result.append(i)
    else:
        min_result.append(i)

if len(min_result) == 0:
    min_result.append(100)
elif len(max_result) == 0:
    max_result.append(100)

print(max(max_result), min(min_result))