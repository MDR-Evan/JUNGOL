animal = []
count = 0

while count < 4:
    animal.extend(input("Input? ").split())
    count += 1

color = animal[::2]
animal = animal[1::2]

print("Color:", color)
print("Animal:", animal)