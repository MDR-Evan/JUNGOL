num = []

num1, index1 = map(int, input().split())
num2, index2 = map(int, input().split())

for i in range(index1):
    num.append(num1)

for i in range(index2):
    num.append(num2)

print(num)