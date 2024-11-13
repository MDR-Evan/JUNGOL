num = list(map(int, input().split()))
odd = []
even = []

for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(max(even), min(odd))