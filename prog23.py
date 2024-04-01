class Account:
    def __init__(self,acc_no,acc_bal):
        self.acc_no = acc_no
        self.__acc_bal = acc_bal#__ is used to make private
        print(self.__acc_bal)

a1 = Account(12345,"abcde")
print(a1.acc_no)
print(a1.__acc_bal)