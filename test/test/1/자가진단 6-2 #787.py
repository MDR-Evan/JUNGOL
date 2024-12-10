element = []
for i in range(6):
    element.append((input("Element? ")))
for i in range(6):
    if i % 2 == 0:
        odd = element[0::2]
    else:
        even = element[1::2]

print(odd+even)