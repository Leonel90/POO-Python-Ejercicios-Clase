from bank import Bank

class Transfer(Bank):
    id      = int
    
    def __init__(self, id, ammount, date, typePayment, bankName, identification, numberAccount):
        super().__init__(id, ammount, date, typePayment, bankName, identification, numberAccount)
        self.bankName       = bankName
        self.identification = identification
        self.numberAccount  = numberAccount