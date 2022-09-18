# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:16:31 2022

@author: antoi
"""
import numpy as np
from opn.convertions.energy_contents import ME, MER
from opn.utils.json_utils import read_json

print("-------------")
# Animal weight
weight = 4.2
# Percentage of wet food
wet_p = 0.8
# Percentage of dry food
dry_p = 0.2
# MER factor (see energy_contents.py)
X = 1.
# animal type
animal = 'cat'

wet = read_json('input_data/food_catalog/cats/Animonda_Carny_Adult_meat_cocktail.json')['Composition per 100g']

_ME_wet = ME(
    wet["Humidity (g)"]['total'],
    wet["Protein (g)"]['total'],
    wet["Fat (g)"]['total'],
    wet["Ashes (g)"]['total'],
    wet["Fibers (g)"]['total'],
    animal
)


dry = read_json('input_data/food_catalog/cats/Eukanuba_Top_Condition_7+_Senior.json')['Composition per 100g']

_ME_dry = ME(
    dry["Humidity (g)"]['total'],
    dry["Protein (g)"]['total'],
    dry["Fat (g)"]['total'],
    dry["Ashes (g)"]['total'],
    dry["Fibers (g)"]['total'],
    animal
)

_MER = np.ceil(MER(weight, X))
quantity_wet = np.ceil(((_MER * wet_p)/_ME_wet)*100)
quantity_dry = np.ceil(((_MER * dry_p)/_ME_dry)*100)

print("{} ({} kg) target {} kcal/day:".format(animal, weight, _MER))
print("  - {} g Wet/day ".format(quantity_wet))
print("  - {} g dry/day ".format(quantity_dry))


