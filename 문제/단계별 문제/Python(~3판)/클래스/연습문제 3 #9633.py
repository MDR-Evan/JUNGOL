from unittest import result


class Score:
    result = []

    def __init__(self, name, kor, eng):
        self.name = name
        self.kor = kor
        self.eng = eng

    def plus(self):
        kor, eng = 0, 0

        for i in range(2):
            kor += self.kor[i]
            eng += self.eng[i]
        result = [kor, eng]

    def out_Inpo(self):
        for i in range(2):
            print("%s %d %d" % (self.name[i], self.kor[i], self.eng[i]))
        print("합계 %d %d" % result[0], result[1])

student = []
for i in range(2):
    name, kor, eng = input().split()
    stuname, kor, eng)
