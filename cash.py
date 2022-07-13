from payment import Payment

class Cash(Payment):
    id  = int
    
    def __init__(self, ammount, id):
        super.__init__(id, ammount)
        self.id = id