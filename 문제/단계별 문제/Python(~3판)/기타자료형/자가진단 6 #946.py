dic = {}
num = int(input())

for i in range(num):
    N, C = input().split()
    dic[N] = C

text = input()

if  text in dic:
    for i in dic.keys():
        if i == text:
            print(dic[i])
else:
    print("Unknown Country")