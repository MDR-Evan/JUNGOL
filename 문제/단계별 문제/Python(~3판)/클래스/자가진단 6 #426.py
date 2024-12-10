class Profile:
    def __init__(self, man):
        self.man = man

    def name_so(self):
        print("name")
        self.man.sort(key=lambda x: x[0])
        for i in self.man:
            print(*i)
        print()

    def weight_so(self):
        print("weight")
        self.man.sort(key=lambda x: x[2], reverse=True)
        for i in self.man:
            print(*i)
        print()

man = []
for i in range(5):
    name, height, weight = input().split()
    height = int(height)
    weight = float(weight)
    man.append((name, height, weight))

profile = Profile(man)
profile.name_so()
profile.weight_so()