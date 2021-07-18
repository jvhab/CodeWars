'''
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths.
Can you help him to find out, how many cakes he could bake considering his recipes?
Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and
returns the maximum number of cakes Pete can bake (integer).
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200).
Ingredients that are not present in the objects, can be considered as 0.
Examples:
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
'''

from typing import Dict
def cakes(recipe: Dict, available: Dict) -> int:
    res = []
    av = available.keys()
    for keys in recipe:
        if keys not in av:
            res.append(0)
        else:
            res.append(available[keys] // recipe[keys])
    return min(res)

recipe = {'butter': 45, 'cocoa': 54, 'milk': 92}
available = {'chocolate': 2227, 'nuts': 4600, 'eggs': 4424, 'apples': 9845, 'pears': 5783, 'crumbles': 5232, 'butter': 9994, 'milk': 9996, 'flour': 719, 'cream': 3779}
print(cakes(recipe, available))

'''
-----BEST PRACTICES-----
#1
def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)

#2
def cakes(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0
'''