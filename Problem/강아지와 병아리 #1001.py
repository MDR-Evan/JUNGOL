while True:
    sum, leg = map(int, input().split())

    if sum == 0 and leg == 0:
        break

    if sum < 0 or sum > 1000 or leg < 0 or leg > 4000:
        print("INPUT ERROR!")
        continue

    dogs = (leg - 2 * sum) // 2
    chickens = sum - dogs

    if dogs >= 0 and chickens >= 0 and (4 * dogs + 2 * chickens == leg):
        print(dogs, chickens)
    else:
        print("0")