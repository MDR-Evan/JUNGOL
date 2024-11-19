def suminus(num1, num2):
    add = num1 + num2
    if num1 > num2:
        minus = num1 - num2
    else:
        minus = num2 - num1
    return add, minus

num1, num2 = map(int, input().split())
add, minus = suminus(num1, num2)

print("두 수의 합 = %d" % add)
print("두 수의 차 = %d" % minus)