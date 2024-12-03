class Information:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Info(self):
        print("당신의 이름은 %s이고 나이는 %s세이군요." % (self.name, self.age))

name = input("당신의 이름은 무엇입니까? ")
age = input("당신의 나이는 몇 살입니까? ")

info = Information(name, age)
info.Info()