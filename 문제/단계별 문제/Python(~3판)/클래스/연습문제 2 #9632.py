class Friend:
    my_name = "문은비"
    my_age = 12

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def friend(self):
        print("당신의 이름 : %s, 나이 : %d" % (Friend.my_name, Friend.my_age))
        print("친구의 이름 : %s, 나이 : %d" % (self.name, self.age))

name, age = input("친한 친구의 이름과 나이를 입력하세요. ").split()
friend = Friend(name, int(age))

friend.friend()