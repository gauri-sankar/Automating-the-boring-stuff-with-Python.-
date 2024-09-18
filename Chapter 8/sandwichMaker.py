#! python3
#sandwichMaker.py - Takes orders for different sandwiches and displays total amount.

import pyinputplus as pyip
import time

#The prices of ingredients
ingredients = {
    'Wheat': 1.00,
    'White': 0.80,
    'Sourdough': 1.20,
    'Chicken': 3.00,
    'Beef': 4.00,
    'Ham': 2.50,
    'Tofu': 2.00,
    'Cheddar': 1.50,
    'Swiss': 1.75,
    'Mozzarella': 1.60,
    'Blue': 2.00,
    'Mayo': 0.50,
    'Mustard': 0.30,
    'Lettuce': 0.40,
    'Tomato': 0.60
}


def sandwichMaker():
    price = 0
    protiens = ['Chicken','Beef','Ham','Tofu']
    addOns = ['Mayo','Mustard','Lettuce','Tomato']
    order = []

    #Selecting the bread type
    response = pyip.inputMenu(['Wheat','White','Sourdough'],prompt='Select bread type\n',numbered=True)
    order.append(response)

    #Selecting protiens
    nos = pyip.inputNum('How many type protiens do you need?(Maximum 3)\n',max=3,min=1)
    for iteration in range(nos):
        response = pyip.inputMenu(protiens,f'Select protien(s)\n',numbered=True)
        order.append(response)
        protiens.remove(response)

    #Selecting Cheese type
    response = pyip.inputYesNo(prompt='Do you want cheese? - ')

    if response  == 'yes':
        response = pyip.inputMenu(['Cheddar','Swiss','Mozarella','Blue'],prompt='Select cheese\n',numbered=True)
        order.append(response)
    
    #Selecting addOns
    response = pyip.inputYesNo(prompt='Do you have addons? - ')

    if  response == 'yes':
        limit = 4
        while True:
            response = pyip.inputMenu(addOns,f'Select add-On(s)\n',numbered=True,blank=True)
            order.append(response)
            addOns.remove(response)
            response = pyip.inputYesNo(prompt='Do you have more add-Ons? - ')
            if  response.lower() =='no' or len(addOns) == 0:
                break
            limit -= 1
    
    #Finding prices
    for item in order:
        price += ingredients[item]

    #Printing the order and price
    print('Your Order'.center(20,'*'))
    for i in range(len(order)):
        print(f'{i+1}.{order[i]}')
    print(f'Order Total: {price}$')

    
sandwichMaker()



