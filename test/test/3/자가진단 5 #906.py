low, high = [], []

num = list(map(int,input().split()))
for i in num:
    if i < 100:
        low.append(i)
    else:
        high.append(i)
if len(low) == 0:
    low.append(100)
elif len(high) == 0:
    high.append(100)

print(max(low), min(high))