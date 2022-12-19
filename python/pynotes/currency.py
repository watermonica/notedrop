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




    

