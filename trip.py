from account import Account
from car import Car
from driver import Driver
from payment import Payment
from rute import Rute
from user import User


class Trip(Car, User, Driver, Rute, Payment):
    id      = int
    
    def __init__(self, idTrip, idUser, idDriver, start, end, kmDistance, typePayment, ammount, date, licence, driver):
        super().__init__(idTrip, idUser, idDriver, start, end, kmDistance, typePayment, ammount, date,licence, driver)
        
        self.idTrip             = idTrip
        