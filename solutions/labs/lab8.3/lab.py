from dealership.car import Car
from dealership.motorcycle import Motorcycle

# create vehicles
vehicle1 = Motorcycle(2016, "Harley Davidson", "Iron 883", 999, 4.8, 51)
vehicle2 = Car(2015, "Toyota", "Prius", 21547, 11.9, 55)

vehicle1.drive(100)
vehicle2.drive(100)

vehicle1.drive(500)
vehicle2.drive(500)
