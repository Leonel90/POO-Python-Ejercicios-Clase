from car import Car

class UberFlash(Car):
    brand       = str
    model       = str
    loadSize    =[]
    loadWei
    
    def __init__(self, license, driver, brand, model):
        super.__init__(license, driver)
        self.brand = brand
        self.model = model