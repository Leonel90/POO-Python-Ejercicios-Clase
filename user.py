from account import Account

class User(Account):
    idUser      = int
    
    
    def __init__(self, idUser, name, dacument, mail, password, gender, numberCell, age):
        super().__init__(name, dacument, mail, password, gender, numberCell, age)
        self.idUser = idUser