from lib2to3.pgen2 import driver

from account import Account


class Car :
    id          = str
    # Tipo de dato cambiado en base a Account (primero importar la informacion)
    driver      = Account("","")
    passager    = str
    brand       = str
    model       = str
    license     = str
    
    def __init__(self,license,driver):
        self.license        = license
        self.driver         = driver