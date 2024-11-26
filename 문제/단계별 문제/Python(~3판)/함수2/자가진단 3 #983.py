def d_cal(a,b):
    t_a = a
    t_b = b

    if a < 0:
        t_a = abs(a)
    if b < 0:
        t_b = abs(b)

    if t_a > t_b:
        print(a)
    else:
        print(b)

def f_cal(a,b):
    t_a = a
    t_b = b

    if a < 0:
        t_a = abs(a)
    if b < 0:
        t_b = abs(b)

    if t_a < t_b:
        print(a)
    else:
        print(b)

d_num1, d_num2 = map(int, input().split())
f_num1, f_num2 = map(float, input().split())

d_cal(d_num1, d_num2)
f_cal(f_num1, f_num2)