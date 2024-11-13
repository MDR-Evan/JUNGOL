num1, num2 = map(int, input("주사위를 던진 결과를 입력하세요. ").split())

if num1 >= 4 and num2 >= 4:
    print("이겼습니다.")
elif num1 >= 4 or num2 >= 4:
    print("비겼습니다.")
else:
    print("졌습니다.")