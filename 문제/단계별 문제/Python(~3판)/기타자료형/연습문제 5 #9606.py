dic = {"사과":1, '배':2, '포도':3}
text = input("문자열을 입력하시오: ")

if text in dic.keys():
    for i in dic.keys():
        if i == text:
            print("%d번" % dic[i])
else:
    print("0번")