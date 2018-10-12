# sample dictionary of drinks

drinks = {'vodka tonic' : {'vodka', 'tonic'}
          , 'margarita' : {'tequila','lime juice', 'triple sec'}
          , 'martini' : {'vodka', 'vermouth'}
          , 'black russian' : {'vodka', 'kahlua'}
          , 'white russian' : {'vodka', 'kahlua', 'cream'}
          , 'manhattan' : {'rye', 'vermouth', 'bitters'}
          , 'screwdriver' : {'orange juice','vodka'}
          }

print(drinks)

print('\n')

drink_names = list(drinks.keys())

drink_ingred = list(drinks.values())

print(drink_ingred)

print(drinks.get('margaritas', "I don't know how to make that!"))

