def num_avg(a, b, c):
    return ((a + b + c) / 3)

num1, num2, num3 = map(int, input("세과목의 점수를 입력하세요. ").split())
print("평균 : %.2f" % num_avg(num1, num2, num3))