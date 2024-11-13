count = 0

while True:
    num = int(input())

    if num == 0 :
        print(count)
        break
    elif num % 3 != 0 and num % 5 != 0 :
        count += 1