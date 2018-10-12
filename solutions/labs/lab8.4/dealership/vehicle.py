class Vehicle(object):
    """ A vehicle for passenger transport """

    wheels = 0

    def __init__(self, data):
        self.year = data["Year"]
        self.make = data["Make"]
        self.model = data["Model"]
        self.odometer = data["Odometer"]
        self.gas = data["Gas"]
        self.mpg = data["MPG"]
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
            return False
