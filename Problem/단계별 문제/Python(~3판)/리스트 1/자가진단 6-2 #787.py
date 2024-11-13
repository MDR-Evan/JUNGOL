count = 0
country = []

while count < 6:
    country.append(input("Element? "))
    count += 1

odd = country[0::2]
even = country[1::2]

print(odd+even)