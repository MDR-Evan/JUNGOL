a,b = map(int,input().split())
if a > b:
    print("입력받은 수 중 큰 수는 %d 이고 작은 수는 %d 입니다." %(a, b))
else:
    print("입력받은 수 중 큰 수는 %d 이고 작은 수는 %d 입니다." % (b, a))