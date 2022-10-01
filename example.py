# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:16:31 2022

@author: antoi
"""

from opn.tools.diet_planning import WeightLossPlanner, DietPlanner
from opn.utils.json_utils import read_json
from opn.utils.animal_utils import Cat


# Animal weight
weight = 5.5
target_weight=4.5
# Percentage of wet food
wet_p = 0.5
# Percentage of dry food
dry_p = 0.5
# animal type
animal = 'cat'
age = 8
is_active = False
is_neutered = True

animal = Cat(weight,age,is_neutered,is_active)

wet = read_json('input_data/food_catalog/cats/wet/Purizon_Adult_Chicken_fillet_with_salmon.json')['Composition per 100g']
dry = read_json('input_data/food_catalog/cats/dry/Purizon_Adult_Chicken_with_fish.json')['Composition per 100g']

#Percentage of total body mass to loose per week, going above 2 can cause health issues
per_week_loss_percentage = 1.25
weight_loss_plan = WeightLossPlanner(
    animal, target_weight, dry, wet, dry_p, wet_p,
    per_week_loss_percentage=per_week_loss_percentage
).plan_diet()

# For weight loss
print(weight_loss_plan)
"""
              Weight  Target kcal (ME)  Wet food (g) / day  Dry food (g) / day
2022-09-22       5.5             239.0               115.0                33.0
2022-09-29   5.43125             237.0               114.0                32.0
2022-10-06  5.363359             235.0               113.0                32.0
2022-10-13  5.296317             233.0               112.0                32.0
2022-10-20  5.230113             230.0               111.0                31.0
2022-10-27  5.164737             228.0               110.0                31.0
2022-11-03  5.100178             226.0               109.0                31.0
2022-11-10  5.036426             224.0               108.0                31.0
2022-11-17   4.97347             222.0               107.0                30.0
2022-11-24  4.911302             220.0               106.0                30.0
2022-12-01  4.849911             218.0               105.0                30.0
2022-12-08  4.789287             216.0               104.0                29.0
2022-12-15  4.729421             214.0               103.0                29.0
2022-12-22  4.670303             212.0               102.0                29.0
2022-12-29  4.611924             210.0               101.0                29.0
2023-01-05  4.554275             208.0               100.0                28.0
2023-01-12       4.5             206.0               100.0                28.0
"""

animal = Cat(target_weight, age, is_neutered, is_active)
diet_plan = DietPlanner(animal, dry, wet, 0.5, 0.5).plan_diet()

# For maintenance
print(diet_plan)
"""
   Weight  Target kcal (ME)  Wet food (g) / day  Dry food (g) / day
0     4.5             217.0               105.0                30.0
"""