sum = 0
avg = 0
count = 1

while True:
    num = int(input())

    if num == 0:
        break
    else:
        if num % 2 == 1:
            sum += num
            avg = float(sum / count)
            count += 1
print("홀수의 합 = %d" %(sum))
print("홀수의 평균 = %d" %(avg))