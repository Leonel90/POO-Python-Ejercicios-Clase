from bank import Bank

class Card(Bank):
    cardNUmber          = int
    identification      = int
    cardDate            = int
    cardSecurityCode    = int
    
    def __init__(self, id, typePayment, ammount, date, bankName, identification, numberAccount, cardNumber, cardDate, cardSecurityCode):
        super().__init__(id, typePayment, ammount, date, bankName, identification, numberAccount)
        self.cardDate           = cardDate
        self.cardNUmber         = cardNumber
        self.cardSecurityCode   = cardSecurityCode