Month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Spacial_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    Y = int(input("YEAR = "))
    M = int(input("MONTH = "))

    if M == 0:
        break
    elif M > 12 or M < 0:
        print("잘못 입력하였습니다.\n")
    else:
        if Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0:
            print(f"입력하신 달의 날 수는 {Spacial_day[M-1]}일입니다.\n")
        else:
            print(f"입력하신 달의 날 수는 {Month_day[M-1]}일입니다.\n")