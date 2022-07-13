from car import Car

class UberConfort(Car):
    numberPassaggers        = int
    carAccepted              = []
    seatMaterial             = []
    
    def __init__(self, license, driver, carAccepted, seatMaterial, numberPassaggers):
        super.__init__(license, driver)
        self.carAccepted        = carAccepted
        self.seatMaterialç      = seatMaterial
        self.numberPassaggers   = numberPassaggers