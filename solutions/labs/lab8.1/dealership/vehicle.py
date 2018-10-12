

class Vehicle(object):
    """ A vehicle for passenger transport """

    wheels = 4

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
        print("Vehicle: " + str(self.year) + " " + self.make + " " + self.model)