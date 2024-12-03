class Idcard:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def out_info(self):
        print("name : %s" % self.name)
        print("tel : %s" % self.phone)
        print("addr : %s" % self.address)

name, tel, addr = input().split()

idcard = Idcard(name, tel, addr)
idcard.out_info()