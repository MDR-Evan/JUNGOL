n = list(map(int, input().split()))
temp = 0

for i in n:
    temp += i

result = temp / len(n)

print("%.2f" % result)