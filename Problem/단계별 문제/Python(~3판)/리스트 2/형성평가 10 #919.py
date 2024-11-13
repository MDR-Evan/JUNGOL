word = []
result = []

while len(word) < 5:
    word.append(input().strip())

text = input()
string = input()

for i in word:
    if text in i or string in i:
        result.append(i)

if len(result) != 0:
    for i in result:
        print(i)
else:
    print("none")