class Vehicle(object):
    """ A vehicle for passenger transport """

    wheels = 0

    def __init__(self, year, make, model, miles, gas, mpg):
        self.year = year
        self.make = make
        self.model = model
        self.odometer = miles
        self.gas = gas
        self.mpg = mpg
        print("Vehicle: " + str(self.year) + " " + self.make + " " + self.model)
        print("wheels: " + str(self.wheels))

    def drive(self, distance):
        fuelToBeUsed = distance / self.mpg
        print("fuel to be used: " + str(fuelToBeUsed))
        if self.gas >= fuelToBeUsed:
            self.odometer += distance
            print("Odometer: " + str(self.odometer))
            self.gas -= fuelToBeUsed
            print("gas left: " + str(self.gas))
        else:
            print("Not enough gas!!!")
