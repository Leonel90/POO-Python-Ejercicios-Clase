from payment import Payment
from bank import Bank

class Transfer(Bank, Payment):
    id      = int
    
    def __init__(self, id, ammount, date, bank, identification, numberAccount):
        super().__init__(id, ammount, date, bank, identification, numberAccount)