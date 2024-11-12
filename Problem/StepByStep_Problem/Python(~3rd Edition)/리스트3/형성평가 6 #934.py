num = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
sum = []
result = 0

for i in num:
    print(*i)

for i in num:
    for j in i:
        sum.append(j)

for i in sum:
    result = result + i
print(result)

# for i in range(4):
#     for j in range(3):
#         print(num[i][j], end=' ')
#         result = result + num[i][j]
#     print()
# print(result)
