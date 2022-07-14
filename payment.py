class Payment:
    id              = int
   # id      = Cash("","")
    ammount         = int
    date            = str
    typePayment     = []
    
    def __init__(self, id, ammount, date, typePayment):
        self.id             = id
        self.ammount        = ammount
        self.date           = date
        self.typePayment    = typePayment