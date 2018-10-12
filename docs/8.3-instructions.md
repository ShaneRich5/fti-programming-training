1. Copy the files from the previous lab.
2. Add parameters to the Vehicle constructor for miles, gas and mpg and assign each to a properties odometer, gas and mpg respectively.
3. In "lab.py", pass the following additional arguments.
    1. The Harley currently has 999 miles, a 4.8 gallon gas tank and gets 51 mpg 
    2. The Toyota has 21,547 miles, an 11.9 gallon tank and gets 55 mpg.

4. Next, create a method called "drive" which should accept an argument named "distance" and then increment the odometer by the provided distance. 
5. Print out the new odometer reading.
6. Drive each car 100 miles.
7. Update the drive method so the "gas" property is decreased to reflect the amount of fuel left in the tank and execute the script again.
8. Now, update the drive method to double check there is enough gas in the tank to drive the distance provided.