drinks = {'vodka tonic' : {'vodka', 'tonic'}
          , 'margarita' : {'tequila','lime juice', 'triple sec'}
          , 'martini' : {'vodka', 'vermouth'}
          , 'black russian' : {'vodka', 'kahlua'}
          , 'white russian' : {'vodka', 'kahlua', 'cream'}
          , 'manhattan' : {'rye', 'vermouth', 'bitters'}
          , 'screwdriver' : {'orange juice','vodka'}
          }

#Using your drink-list dictionary, make all of values Sets instead of Lists


#Print all of the ingredient sets

print(drinks.values())



# If your drink lists don't include White and Black Russians, add them.



# Print the common ingredients in the Russians.



print("what do white and black russians have in common?")
print(drinks['white russian'] & drinks['black russian'])


# What does a White Russian have that a Black Russian does not?

print("what does a white russian have that a black russian does not?")
print(drinks['white russian'] - drinks['black russian'])



# You're having a party tonight and plan on making all of these drinks.  Print a shopping list of the unique ingredients you'll need.
# (for now, you'll do this in a very inefficient, tedious way - make an explicit request for the ingredients for each of your drinks, and concatenate those together)

groceryset = set(drinks['vodka tonic'])

groceryset = groceryset.union(set(drinks['white russian']))
groceryset = groceryset.union(drinks['white russian'])
groceryset = groceryset.union(drinks['black russian'])
groceryset = groceryset.union(drinks['screwdriver'])
groceryset = groceryset.union(drinks['martini'])
groceryset = groceryset.union(drinks['manhattan'])
groceryset = groceryset.union(drinks['margarita'])


print(groceryset)
