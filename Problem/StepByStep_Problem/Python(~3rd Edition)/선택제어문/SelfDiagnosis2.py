height = int(input())
weight = int(input())

temp = weight + 100 - height
print(temp)
if temp >= 0:
    print("Obesity")