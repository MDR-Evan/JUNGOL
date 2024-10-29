day = [28, 30, 31]

month = int(input())

if (month < 8):
    if (month % 2 == 0):
        if (month == 2):
            print(day[0])
        else:
            print(day[1])
    else:
        print(day[2])
else:
    if (month % 2 == 0):
        print(day[2])
    else:
        print(day[1])