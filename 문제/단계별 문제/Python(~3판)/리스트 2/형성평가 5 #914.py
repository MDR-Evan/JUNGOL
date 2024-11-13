num = list(map(int, input().split()))
result = []

for i in num:
    if i % 5 == 0:
        result.append(i)

print(f"Multiples of 5 : {len(result)}")
print(f"sum : {sum(result)}")
print("avg : %.1f" % (sum(result) / len(result)))