from unicodedata import name


class Account :
    id          = int
    name        = str
    dacument    = int
    mail        = str
    
    #metodo constructor en Python
    def __init__(self, name, dacument):
        self.name       = name
        self.dacument   = dacument