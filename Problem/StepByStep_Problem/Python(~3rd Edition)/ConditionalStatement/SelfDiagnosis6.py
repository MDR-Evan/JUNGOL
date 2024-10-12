gender, age = input().split()
age = int(age)
if gender == "M" and age >= 18:
    print("MAN")
elif gender == "F" and age >= 18:
    print("WOMAN")
elif gender == "M" and age < 18:
    print("BOY")
else:
    print("GIRL")