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


for drink_name in drink_names:
    print("Ingredients to make a " + drink_name.capitalize() + ":")
    for ingredient in list(drinks[drink_name]):
        print(ingredient)
    print('\n')