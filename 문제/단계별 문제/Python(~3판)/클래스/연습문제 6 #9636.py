class Profile:
    def __init__(self, man):
        self.man = man

    def name_so(self):
        self.man.sort(key= lambda x: x[0])
        for i in self.man:
            print(*i)

    def height_so(self):
        self.man.sort(key= lambda x: x[1])
        for i in self.man:
            print(*i)

    def weight_so(self):
        self.man.sort(key= lambda x: x[2], reverse=True)
        for i in self.man:
            print(*i)

man = []
for i in range(5):
    name, height, weight = input().split()
    height = int(height)
    weight = float(weight)
    man.append((name, height, weight))

profile = Profile(man)
profile.height_so()
print()
profile.weight_so()
print()
profile.name_so()
