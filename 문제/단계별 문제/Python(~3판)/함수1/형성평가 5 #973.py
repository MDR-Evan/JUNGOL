score = []
total = []

def cal(a, b, c):
    print(*a, sum(a))
    print(*b, sum(b))
    print(*c, sum(c))
    for i in range(3):
        print(a[i]+ b[i] + c[i], end=" ")
        total.append(a[i] + b[i] + c[i])
    print(sum(total))

for i in range(3):
    sc = list(map(int, input().split()))
    score.append(sc)

cal(score[0], score[1], score[2])
