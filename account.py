from codecs import getencoder
from curses import ACS_GEQUAL
from unicodedata import name


class Account :
    id          = int
    name        = str
    dacument    = int
    mail        = str
    password    = str
    gender      = str
    numberCell  = int
    age         = int
    
    #metodo constructor en Python
    def __init__(self, name, dacument,  mail, password, gender, numberCell, age):
        self.name       = name
        self.dacument   = dacument