from unicodedata import name


class Account :
    id          = int
    name        = str
    dacument    = int
    mail        = str
    
    def __init__(self, name, dacument):
        self.name       = name
        self.dacument   = dacument