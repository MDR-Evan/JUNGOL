li = []
result = []

for i in range(10):
    li.append(input().strip())
text = input()

for i in li:
    if text == i[-1]:
        result.append(i)

if len(result) != 0:
    for i in result:
        print(i)