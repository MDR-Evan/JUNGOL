class Point:
    x, y = 0, 0

    def __init__(self, data):
        self.data = data

    def cal(self):
        for i in range(len(self.data)):
            Point.x += int(data[i][0])
            Point.y += int(data[i][1])
        Point.x = Point.x / len(self.data)
        Point.y = Point.y / len(self.data)

    def out_info(self):
        print("중심점의 위치 = (%.1f, %.1f)" % (self.x, self.y))

data = []
for i in range(2):
    data.append(list(map(int, input("점의 좌표는?(x, y) ").split())))

point = Point(data)
point.cal()
point.out_info()