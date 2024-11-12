num = int(input())
score = list(map(int, input().split()))

if len(score) == num:
    score.sort(reverse=True)

for i in score:
    print(i)