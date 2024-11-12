nature = ('Forest', 'Ocean', 'Mountain', 'Plain')
num = int(input())

if 1 <= num and num <= 4:
    num = num - 1
    print(nature[num])
else:
    print("Input Error")