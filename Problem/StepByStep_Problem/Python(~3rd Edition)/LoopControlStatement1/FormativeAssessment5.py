while True :
    width = int(input("Width = "))
    height = int(input("Height = "))
    area = float((width * height) / 2)

    print("Triangle Area = %.1f" %(area))

    re = input("Continue? ")

    if re != "Y" and re != "y" :
        break