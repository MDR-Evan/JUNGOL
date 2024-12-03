import math

def cal(num):
    num.sort(reverse=True)
    print("%d %d %d" % (math.ceil(num[0]), math.floor(num[2]), round(num[1])))

num = list(map(float, input("").split()))
cal(num)


