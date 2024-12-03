from logging import fatal


class Idcard:
    def __init__(self, data):
        self.data = data

    def so(self):
        self.data.sort(key=lambda x:x[0])

    def out_Inpo(self):
        print("name : %s" % self.data[0][0])
        print("tel : %s" % self.data[0][1])
        print("addr : %s" % self.data[0][2])

data = []
for i in range(3):
    data.append(list(input().split()))

idcard = Idcard(data)
idcard.so()
idcard.out_Inpo()