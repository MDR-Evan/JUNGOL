odd = 0
even = 0

while True :
    num = int(input())

    if num == 0 :
        break
    elif num % 2 == 0 :
        even += 1
    else :
        odd += 1

print("odd : %d" %(odd))
print("even : %d" %(even))