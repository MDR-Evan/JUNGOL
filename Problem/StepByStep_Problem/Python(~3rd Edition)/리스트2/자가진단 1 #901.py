score = [85.6, 79.5, 83.1, 80.0, 78.2, 75.0]

a, b = map(int, input().split())

if 1 <= a <= 6 and 1 <= b <= 6:
    result = score[a-1] + score[b-1]
    print(result)