text = ["flower", "rose", "lily", "daffodil", "azalea"]
result = []

word = input()

for i in text:
    if word == i[1:2] or word == i[2:3]:
        result.append(i)

if len(result) != 0:
    for i in result:
        print(i)
    print(len(result))
else:
    print("0")