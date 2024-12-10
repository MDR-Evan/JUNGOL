class Family:
    result_hei, result_wei = 0, 0

    def __init__(self, family):
        self.family = family

    def hei(self):
        for i in range(len(self.family)):
            Family.result_hei = Family.result_hei + self.family[i][0]
        print("height : %dcm" % ((Family.result_hei / len(self.family)) + 5))

    def wei(self):
        for i in range(len(self.family)):
            Family.result_wei = Family.result_wei + self.family[i][1]
        print("weight : %.1fkg" % ((Family.result_wei / len(self.family)) - 4.5))

man = []
for i in range(2):
    height, weight = map(float, input().split())
    man.append((int(height), weight))

family = Family(man)
family.hei()
family.wei()