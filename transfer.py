from payment import Payment
from bank import Bank

class Transfer(Payment, Bank):
    def __init__(self, id, ammount, bank, inde):
        super().__init__(id, ammount)