class BankAccountReceivingEnd:
    ##private
    __routingnumber = None
    __accountnumber = None

    def __init__(self, walletName, walletBalance):
        self.walletName = walletName
        self.walletBalance = walletBalance

    def displayBalance(self):
        return(self.walletBalance)

    def sendFunds(self, amount, recievingUser):
        self.walletBalance -= amount
        recievingUser.walletBalance += amount


a = BankAccountReceivingEnd('a', 100)
b = BankAccountReceivingEnd('b', 100)
a.sendFunds(20, b)
print(str(a.displayBalance()))
print(str(b.displayBalance()))
b.sendFunds(34, a)
print(str(a.displayBalance()))
print(str(b.displayBalance()))



    

