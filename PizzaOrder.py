pizza_order1 = {'Name': 'John',
                'Jalapenos': 12,
                'Peppers': 2, 
                'Mushroom': 12, 
                'Chilli': 10} 

pizza_order2 = {'Name': 'Amy', 
                'Jalapenos': 0, 
                'Peppers': 10, 
                'Mushroom': 12, 
                'Chilli': 5} 


def merge(p1,p2,name):
    newpizza = {}

    for k in (p1):
        newpizza[k] = [p1[k] + p2[k]]
        newpizza['Name'] = name
    return newpizza

userinput3 = input("What size would you like your Pizza? \n A - Small - 12 inch \n B - Medium - 15 inch \n C - Large - 20 inch \n:")
def pizzasize(p,size):
    if size == 'A':
        p['Size'] = 12
    elif size == 'B':
        p['Size'] = 15
    elif size == 'C':
        p['Size'] = 20


userinput1 = input("Please select crust preference   1-Thick   2-Thin :  ")

def crust (p,x):
    if x == '1':
        p['Crust'] = 'Thick'
    else:
        p['Crust'] = 'Thin'

userinput2 = input("Would you like any extra toppings? \n 1 - Extra Jalapenos \n 2 - Extra Peppers \n 3 - Extra Mushrooms \n 4 - Extra Chilli's \n 5 - No Extra's  \n : ")
def extratoppings(p,topping):
    if topping == '1':
        p['Jalapenos'] += 8
    elif topping == '2':
        p['Peppers'] += 8
    elif topping == '3':
        p['Mushroom'] += 8
    elif topping == '4':
        p['Chilli'] += 8
    elif topping == '5':
        p['Peppers'] += 0




pizza_order3 = merge(pizza_order1,pizza_order2, 'Steve')    ### Merge Pizza

pizzasize(pizza_order1,userinput3)
crust(pizza_order1,userinput1)    
extratoppings(pizza_order1,userinput2)                                 ### Thincrust
print(pizza_order1)
print("\n\n", pizza_order3)
