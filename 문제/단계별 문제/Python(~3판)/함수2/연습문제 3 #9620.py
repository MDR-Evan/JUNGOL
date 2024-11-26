def d_cal(a, b):
    print("두 정수의 차 : %d" % abs(a - b))
def f_cal(a, b):
    print("두 실수의 차 : %f" % abs(a - b))

d_num1, d_num2 = map(int, input().split())
f_num1, f_num2 = map(float, input().split())

d_cal(d_num1, d_num2)
f_cal(f_num1, f_num2)