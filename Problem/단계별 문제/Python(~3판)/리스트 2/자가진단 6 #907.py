num = list(map(int,input().split()))
even = []
odd = []

for i in range(0,len(num)):
    if i % 2 != 0:
        even.append(num[i])
    else:
        odd.append(num[i])

print(f"sum : {sum(even)}")
print(f"avg : {(sum(odd) / len(odd))}")

