text = input()

for i in range(len(text)):
    print(text[1+i::]+text[:i+1:])