sum = 0
avg = 0
count = 0

while True :
    num = int(input())

    sum += num
    count += 1
    avg = float(sum / count)

    if num >= 100 :
        print(sum)
        print("%.1f" % (avg))
        break