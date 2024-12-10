class Triangle:
    x, y = 0, 0

    def __init__(self, data):
        self.data = data

    def calc(self):
        for i in range(len(self.data)):
            if i % 2 == 0:
                Triangle.x += self.data[i]
            else:
                Triangle.y += self.data[i]
        Triangle.x = Triangle.x / 3
        Triangle.y = Triangle.y / 3

    def out_info(self):
        print("(%.1f, %.1f)" % (Triangle.x, Triangle.y))

data = list(map(float, input().split()))

triangle = Triangle(data)
triangle.calc()
triangle.out_info()