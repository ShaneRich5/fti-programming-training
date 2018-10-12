class Vehicle(object):
    """ A vehicle for passenger transport """

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        print("Vehicle: " + str(self.year) + " " + self.make + " " + self.model)


# create vehicles
vehicle1 = Vehicle(2016, "Harley Davidson", "Iron 883")
vehicle2 = Vehicle(2015, "Toyota", "Prius")
