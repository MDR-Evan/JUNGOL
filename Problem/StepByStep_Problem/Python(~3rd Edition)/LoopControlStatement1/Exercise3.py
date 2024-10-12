while True :
    score = int(input("점수를 입력하세요. "))

    if 0<= score and score <= 100 :
        if score >= 80 :
            print("축하합니다. 합격입니다.")
        elif score < 80 :
            print("죄송합니다. 불합격입니다.")
    else :
        break