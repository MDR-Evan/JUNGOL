n = int(input())
result = 0

for i in range(n+1):
    if (i % 5 == 0):
        result += i

print(result)