num = list(map(float, input().split()))
sum = sum(num)
mul = 1
for i in num:
    mul = mul * i
result = (sum, mul)
print(result)
