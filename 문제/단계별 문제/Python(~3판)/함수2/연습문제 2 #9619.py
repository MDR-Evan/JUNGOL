def test(a):
    avg = sum(a) / 3
    result = "합격"

    for i in a:
        if i < 40 or avg < 60:
            result = "불합격"
            break

    print("축하합니다. %s입니다." % result)

score = list(map(int,input("3과목의 점수를 입력하세요. ").split()))
test(score)
