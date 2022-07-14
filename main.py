from pprint import pprint
from account import Account
from car import Car
from cash import Cash
from uberConfort import UberConfort
from uberX import UberX


if __name__ == "__main__":
    #print ("Hola mundo")
    
    car = Car("PBO5555", Account("Leonel Sangolquiza", "0603796434"))
    
    print(vars(car))
    print(vars(car.driver))
    
    uberX = UberX("PCC-12345", Account("Manuelita", "555555555"), "Chevrolet", "Spark")
    print(vars(uberX))
    print(vars(uberX.driver))
    
    uberConfort = UberConfort("PJK-4561", Account("Jose", "123456789"), "Dodge", "Cuero", "6")
    print(vars(uberConfort))
    print(vars(uberConfort.driver))
    
    pagoDinero = Cash("1", "14-7-2022", "20", "Cash")
    print(vars(pagoDinero))
    print(pagoDinero.date)
    
   # uberX = UberX("PCC-12345", Account("Manuelita", "5555555555"), "Chevrolet", "Spark")
    #print(vars(uberX))
    
    
    #uberConfort = UberConfort("pjk-4578", Account("José", "1234569873", ""), "Dodge", "Cuero", "6")
    #print(vars(uberConfort))
    #print(vars(uberConfort.driver))
    
    #pagoDinero = Cash("1", "14-07-2022", "20", "Cash")
    #print(vars(pagoDinero))
    #print(pagoDinero.date)