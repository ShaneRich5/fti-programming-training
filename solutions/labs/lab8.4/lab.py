from dealership.car import Car
from dealership.motorcycle import Motorcycle
import json

# load cars data
with open('cars.json') as json_data:
    carsData = json.load(json_data)

# create vehicles and drive each 100 miles
carsDriven = 0

for carData in carsData:
    car = Car(carData)
    result = car.drive(100)
    if result != False:
        carsDriven += 1

# output number of cars driven
print("Cars driven: " + str(carsDriven))
print("Cars not driven: " + str(len(carsData) - carsDriven))
