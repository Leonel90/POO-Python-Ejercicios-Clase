class Driver(Account):
    id      = int
    license = str
    
    
    def __init__(self, id, name, dacument, mail, password, gender, numberCell, age):
        super().__init__(name, dacument, mail, password, gender, numberCell, age)
        self.id         = id
        self.license    = license