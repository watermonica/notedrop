class BankAccountReceivingEnd:
    ##private
    __routingnumber = None
    __accountnumber = None

    def __init__(self, walletName, walletBalance):
        self._walletName = walletName
        self._walletBalance = walletBalance

    def displayBalance(self):
        return(self._walletBalance)

    