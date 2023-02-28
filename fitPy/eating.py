import math

def gramsToOz(g):
    return g * 0.035274
def ozToGrams(o):
    return o / 0.035274

ingredients = {
    'egg' : {
        'serv' : 100, #grams
        'cals' : 148,
        'prot' : 10, #grams
        'pkg' : 60 #grams
        },
    'egg whites' : {
        'serv' : 100, #grams
        'cals' : 52,
        'prot' : 11, #grams
        'pkg' : ozToGrams(32), #grams
        'unit' : '32oz package'
        },
    'bell pepper' : {
        'serv' : 100, #grams
        'cals' : 0,
        'prot' : 0, #grams
        'pkg' : 150 #grams
        },
    'onion' : {
        'serv' : 100, #grams
        'cals' : 0,
        'prot' : 0, #grams
        'pkg' : 150 #grams
        },
    'low fat cottage' : {
        'serv' : 100, #grams
        'cals' : 0,
        'prot' : 0, #grams
        'pkg' : ozToGrams(24), #grams
        'unit' : '24oz package'
        },
    'fat free cheddar' : {
        'serv' : 100, #grams
        'cals' : 0,
        'prot' : 0, #grams
        'pkg' : ozToGrams(7), #grams
        'unit' : '7oz package'
        },
    'chicken breast' : {
        'serv' : 100, #grams
        'cals' : 0,
        'prot' : 0, #grams
        'pkg' : ozToGrams(8) #grams
        },
    'quinoa' : {
        'serv' : 100, #grams
        'cals' : 0,
        'prot' : 0, #grams
        'pkg' : ozToGrams(12), #grams
        'unit' : '12oz package'
        },
    'broccoli' : {
        'serv' : 100, #grams
        'cals' : 0,
        'prot' : 0, #grams
        'pkg' : 1 #grams
        },
    'turkey bacon' : {
        'serv' : 100, #grams
        'cals' : 0,
        'prot' : 0, #grams
        'pkg' : 1, #grams
        'unit' : 'slice'
        },
    'ham' : {
        'serv' : 100, #grams
        'cals' : 0,
        'prot' : 0, #grams
        'pkg' : ozToGrams(8), #grams
        'unit' : '8oz package'
        }   
    }

recipes = {
    'breakfast burrito' : {
        'egg whites' : {
            'meas' : 150,
            'unit' : 'g'
            },
        'egg' : {
            'meas' : 1,
            'unit' : 'pkg'
            },
        'fat free cheddar' : {
            'meas' : 70,
            'unit' : 'g'
            },
        'low fat cottage' : {
            'meas' : 90,
            'unit' : 'g'
            },
        'bell pepper' : {
            'meas' : 50,
            'unit' : 'g'
            },
        'onion' : {
            'meas' : 50,
            'unit' : 'g'
            },
        'turkey bacon' : {
            'meas' : 2,
            'unit' : 'pkg'
            },
        'ham' : {
            'meas' : 2,
            'unit' : 'oz'
            }  
        }
    }

menu = {
    'breakfast burrito' : {
        'noah' : {
            'servs' : 5,
            'size' : 1
            },
        'lauren' : {
            'servs' : 2,
            'size' : 1
            }
        },
    'lunch' : {
        'noah' : {
            'servs' : 5,
            'size' : 1
            },
        'lauren' : {
            'servs' : 5,
            'size' : 0.5
            },
        'karen' : {
            'servs' : 5,
            'size' : 0.5
            }
        }
    }

def shoppingList():
    cart = {}
    for meal in menu:
        if meal not in recipes:
            print("We don't have a recipe for " + meal + "!")
            continue
        
        # calculate the quanitity we need to make
        qty = 0
        for person in menu[meal]:
            qty += menu[meal][person]['servs'] * menu[meal][person]['size']

        print(meal + ": " + str(qty))

        for ingredient in recipes[meal]:
            if ingredient not in ingredients:
                print("We don't have data for " + ingredient + "!")
                continue
            
            unit = ''
            meas = 0
            if recipes[meal][ingredient]['unit'] == 'g':
                meas = (recipes[meal][ingredient]['meas'] * qty) / ingredients[ingredient]['pkg']                        
            elif recipes[meal][ingredient]['unit'] == 'oz':
                meas = ozToGrams(recipes[meal][ingredient]['meas'] * qty) / ingredients[ingredient]['pkg']
            elif recipes[meal][ingredient]['unit'] == 'pkg':
                meas = recipes[meal][ingredient]['meas'] * qty
            else:
                print(recipes[meal][ingredient]['unit'] +
                      " units are not recognized for " +
                      recipes[meal][ingredient] +
                      "!")
                continue

            # round up
            meas = math.ceil(meas)
                
            if ingredient not in cart:
                if 'unit' in ingredients[ingredient]:
                    unit = ingredients[ingredient]['unit']
                else:
                    unit = ingredient

                cart[ingredient] = {
                    'qty' : meas,
                    'unit': unit
                    }
            else:
                cart[ingredient]['qty'] += meas

    # print shopping list\
    print("   Shopping List")
    print("-------------------")
    for item in cart:
        entry = str(cart[item]['qty']) + " " + cart[item]['unit']

        if cart[item]['qty'] > 1:
            entry += 's'

        if item != cart[item]['unit']:
            entry += " of " + item

        print(entry)
                     

shoppingList()
