class Score:
    def __init__(self, score):
        self.score = score

    def calc(self):
        result = []
        for i in self.score:
            total = sum(i[1:])
            total_result = i + (total, )
            result.append(total_result)
        self.score = result

    def so(self):
        self.score.sort(key=lambda x: x[4], reverse=True)
        for i in self.score:
            print(*i)

score = []
count = int(input())
for i in range(count):
    name, score1, score2, score3 = input().split()
    score.append((name, int(score1), int(score2), int(score3)))

score = Score(score)
score.calc()
score.so()