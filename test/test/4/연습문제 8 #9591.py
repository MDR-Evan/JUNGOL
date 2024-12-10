text = []

print("단어 5개를 입력하세요.")
for i in range(5):
    text.append(input())
for i in (sorted(text)):
    print(i)