text = []

for i in range(5):
    text.append(input())

text.sort(reverse=True)

for i in text:
    print(i)