from payment import Payment
class Bank(Payment):
    bankName            = str
    identification      = str
    numberAccount       = int
    
    def __init__(self, id, ammount, date, typePayment, bankName, identification, numberAccount):
        super().__init__(id, ammount, date, typePayment)
        self.bankName           = bankName
        self.identification     = identification
        self.numberAccount      = numberAccount