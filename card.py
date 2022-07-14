from bank import Bank

class Card(Bank):
    cardNUmber      = int
    identification  = int
    cardDate        = int
    
    def __init__(self, id, ammount, date, bank, identification, numberAccount):
        super().__init__(id, ammount, date, bank, identification, numberAccount)