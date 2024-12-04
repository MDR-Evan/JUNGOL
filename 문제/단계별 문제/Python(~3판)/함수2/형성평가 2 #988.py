import math

def cal(num):
    count = 0
    result = []
    for i in num:
        result.append(math.sqrt(i))

    if result[0] < result[1]:
        result[0], result[1] = result[1], result[0]

    result[0] = math.floor(result[0])
    result[1] = math.ceil(result[1])

    while result[1] <= result[0]:
        result[1] += 1
        count += 1

    print(count)

num = list(map(float, input().split()))
cal(num)