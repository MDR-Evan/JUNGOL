sum = 0
avg = 0
count = 0

while True :
    num = int(input())

    if num >= 0 and num <= 100 :
        count += 1
        sum += num
        avg = float(sum/count)
    else :
        print("sum : %d" %(sum))
        print("avg : %.1f" %(avg))
        break