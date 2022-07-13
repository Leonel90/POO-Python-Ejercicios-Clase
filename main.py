from pprint import pprint
from account import Account
from car import Car


if __name__ == "__main__":
    print ("Hola mundo")
    
    car = Car("PBO5555", Account("Leonel Sangolquiza", "0603796434"))
    
    print(vars(car))
    print(vars(car.driver))