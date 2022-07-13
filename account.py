from codecs import getencoder
import mailbox
from this import s
from unicodedata import name


class Account :
    id          = int
    name        = str
    document    = int
    mail        = str
    password    = str
    gender      = str
    numberCell  = int
    age         = int
    
    #metodo constructor en Python
    def __init__(self, name, document, mail, password, gender, numberCell, age):
        self.name       = name
        self.document   = document
        self.mail       = mail
        self.password   = password
        self.gender     = gender
        self.numberCell = numberCell
        self.age        = age