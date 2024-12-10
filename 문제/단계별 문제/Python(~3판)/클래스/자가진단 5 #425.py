class Profile:
    def __init__(self, man):
        self.man = man

    def So(self):
        self.man.sort(key= lambda x: x[1])

    def out_info(self):
        print(*self.man[0])

man = []
for i in range(5):
    data = (input().split())
    name = data[0]
    height = int(data[1])
    man.append((name, height))

profile = Profile(man)
profile.So()
profile.out_info()