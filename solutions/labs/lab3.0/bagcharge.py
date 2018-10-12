#
# if .. elif statement for extra fees to be paid for a luggage bag over 50 pounds.

# If the bag is under 50 lbs, print "free bag!"
# If the bag exceeds 50lbs but not 75, tell them they'll be charged an extra $25.
# If it's over 75lbs, tell them the extra fee charge is $100 per bag.

def fee_paid(lug_weight):
    charge = ''
    if lug_weight < 50:
        charge = 'Free bag!'
    elif lug_weight <= 75:
        charge = 'Extra charge: $25'
    else:
        charge = 'Extra charge: $100'

    return charge

charge_msg = fee_paid(73)

print(charge_msg)

charge_msg = fee_paid(34)

print(charge_msg)

charge_msg = fee_paid(97)

print(charge_msg)