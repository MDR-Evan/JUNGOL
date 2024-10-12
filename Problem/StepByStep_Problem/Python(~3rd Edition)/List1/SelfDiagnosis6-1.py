count = 0
country = []

while count < 6:
    country.append(input("Element? "))
    count += 1

index = int(input("Index? "))

print(country[index:])