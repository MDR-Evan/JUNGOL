class Bank:
    def __init__(self, money):
        self.money = money

    def result(self):
        print(f"저축왕 {money.index(max(self.money))+1}번 {max(self.money)}원")

money = []
for i in range(5):
    money.append(int(input(f"{i+1}번 저축금액은? ")))

bank = Bank(money)
bank.result()