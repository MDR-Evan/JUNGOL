drink = []

text = input().split()
for i in text:
    drink.append(i)

print(drink[(len(drink)-2):0:-1])