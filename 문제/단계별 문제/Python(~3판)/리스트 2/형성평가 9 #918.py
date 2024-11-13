text = []
result = []

while True:
    text.append(input())
    if text[-1] == '0':
        text.remove('0')
        break

print(len(text))
for i in text:
    if "mo" in i:
        print(i)