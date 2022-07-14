from payment import Payment
from bank import Bank

class Transfer(Bank, Payment):
    id      = int
    
    def __init__(self, id, ammount, bank, inde):
        super().__init__(id, ammount)
        self.id     = id