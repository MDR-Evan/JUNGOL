while True :
    print("1. Korea")
    print("2. USA")
    print("3. Japan")
    print("4. China")
    select = int(input("number? "))

    if select == 1 :
        print("Seoul")
    elif select == 2 :
        print("Washington")
    elif select == 3 :
        print("Tokyo")
    elif select == 4 :
        print("Beijing")
    else :
        print("none")
        break