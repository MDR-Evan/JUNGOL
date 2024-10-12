source_num = 0
source_sum = 0

while True :
    score = int(input())

    if score == 0 :
        break
    else :
        source_num += 1
        source_sum += score
        source_avg = float(source_sum / source_num)

print("입력된 자료의 개수 = %d" % (source_num))
print("입력된 자료의 합계 = %d" % (source_sum))
print("입력된 자료의 평균 = %.2f" % (source_avg))