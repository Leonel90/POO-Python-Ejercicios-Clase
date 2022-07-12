from pprint import pprint
from car import Car


if __name__ == "__main__":
    print ("Hola mundo")
    
    carro = Car()
    carro.id       = 5
    carro.brand    = "Toyota"
    carro.driver   = "Diego"
    carro.passager = 5
    
    
    carro2 = Car()
    carro2.id       = 5
    carro2.brand    = "Fiat"
    carro2.driver   = "Alexander"
    carro2.passager = 4
    carro2.brand    = "Toyota"
    
    print(vars(carro))
    print(vars(carro2))