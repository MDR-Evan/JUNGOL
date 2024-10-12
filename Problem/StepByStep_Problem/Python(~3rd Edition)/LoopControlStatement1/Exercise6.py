while True :
    print("1. 입력하기")
    print("2. 출력하기")
    print("3. 삭제하기")
    print("4. 끝내기")
    select = int(input("작업할 번호를 선택하세요. "))

    if select == 1 :
        print("\n입력하기를 선택하였습니다.\n")
    elif select == 2 :
        print("\n출력하기를 선택하였습니다.\n")
    elif select == 3 :
        print("\n삭제하기를 선택하였습니다.\n")
    elif select == 4 :
        print("\n끝내기를 선택하였습니다.\n")
        break
    else :
        print("\n잘못 선택하였습니다.\n")