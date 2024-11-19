def num_law(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result

m, n = map(int, input().split())
print(num_law(m, n))