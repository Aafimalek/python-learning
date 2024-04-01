class Account:
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc

    def debit(self,amount):
        self.bal -= amount
        print("RS",amount,"was debited")
        print("total balance = ",self.get_bal())

    def credit(self,amount):
        self.bal += amount
        print("RS",amount,"was credited")
        print("total balance = ",self.get_bal())

    def get_bal(self):
        return self.bal 

acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
