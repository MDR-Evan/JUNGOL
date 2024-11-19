dic = {"Pokemon":"Pikachu", "Digimon":"Agumon", "Yugioh":"Black Magician"}
text = input()

if text in dic.keys():
    for i in dic.keys():
        if i == text:
            print(dic[i])
else:
    print("I don't know")