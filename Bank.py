class BankAccount:
    def __init__(self,acc,name,balance):
        self.acc = acc
        self.name = name
        self.balance = balance
    
    def Deposit(self,d):
        self.balance = self.balance + d
        print("balance-",self.balance,"\n")

    def Withdrawal(self,w):
        if(self.balance<w):
            print("insufficient fundss")
        else:
            self.balance = self.balance-w
            print("balance-",self.balance,"\n")
    
    def printstuff(self):
        print("account number-",self.acc)
        print("account name-",self.name)
        print("balance-",self.balance)

class MobileBankAccount(BankAccount):
    def __init__(self,acc,name,balance,mobileno):
        super().__init__(acc,name,balance)
        self.mobileno = mobileno
    
    def Deposit(self, d):
        super().Deposit(d)

    def Withdrawal(self, w):
        super().Withdrawal(w)
    
    def printstuff(self):
        print("Mobile Bank")
        print(self.mobileno)
        super().printstuff()

class InternetBankAccount(BankAccount):
    def __init__(self,acc,name,balance,internetno):
        super().__init__(acc,name,balance)
        self.internetno = internetno
    
    def Deposit(self, d):
        super().Deposit(d)

    def Withdrawal(self, w):
        super().Withdrawal(w)
    
    def printstuff(self):
        print("Internet Bank Account")
        print(self.internetno)
        super().printstuff()


cus1 = MobileBankAccount("qwerty","satay",1000,'9999999')
cus1.Deposit(1000)
cus1.Withdrawal(200)
cus1.printstuff()

cus2 = InternetBankAccount("abcde","varsan",9999,'internetbank123')
cus2.Deposit(1000)
cus2.Withdrawal(200)
cus2.printstuff()

