text = []

for i in range(5):
    text.append(input())
for i in sorted(text, reverse=True):
    print(i)