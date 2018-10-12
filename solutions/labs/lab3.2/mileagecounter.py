def mile_fmt(mile_in):
    mile_out = str(mile_in)
    mile_out = mile_out[:len(mile_out)-3] + ',' + mile_out[-3:]

    return mile_out

mileage = 0

while mileage < 200000:
    if mileage % 10000 == 0:
        print("Still driving... at " + mile_fmt(mileage) + " miles...")
    mileage += 1000

print("...and stop!  You're at 200k miles")