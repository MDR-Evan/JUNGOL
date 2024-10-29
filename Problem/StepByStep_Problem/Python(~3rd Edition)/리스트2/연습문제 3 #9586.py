source = ["champion", "tel", "pencil", "jungol", "olympiad", "class", "information", "lesson", "book", "lion"]
result = []

text = input("문자를 입력하세요. ")

for i in source:
    if text == i[0]:
        result.append(i)

if len(result) != 0:
    for i in result:
        print(i)
else:
    print("찾는 단어가 없습니다.")