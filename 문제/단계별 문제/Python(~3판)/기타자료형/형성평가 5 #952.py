dic = {}

num = int(input())
for i in range(num):
    key, value = input().split()
    dic[key] = value

text = input()

if text in dic.keys():
    for i in dic.keys():
        if i == text:
            print(dic[i])