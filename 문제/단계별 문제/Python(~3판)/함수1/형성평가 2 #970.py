def plus(a):
    result = 0

    for i in range(a+1):
        result = result + i
    return result

num = int(input())
print(plus(num))