a, b, c = map(int, input("세 수를 입력하세요. ").split())
if a > b and a > c:
    print("입력받은 수중 가장 큰 수는 %d입니다." %(a))
elif b > c and b > a:
    print("입력받은 수중 가장 큰 수는 %d입니다." %(b))
else:
    print("입력받은 수중 가장 큰 수는 %d입니다." %(c))