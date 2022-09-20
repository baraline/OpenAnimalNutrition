# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 22:43:37 2022

@author: antoi
"""
import warnings
import pandas as pd
import numpy as np

from datetime import datetime, timedelta

from opn.convertions.energy_contents import ME, MER

class WeightLossPlanner():
    """
    
    Example
    -------
    
    from opn.utils.json_utils import read_json
    from opn.utils.animal_utils import Animal
    animal = Animal('cat',12,8,False,False)
    wet = read_json('input_data/food_catalog/cats/Animonda_Carny_Adult_meat_cocktail.json')['Composition per 100g']
    dry = read_json('input_data/food_catalog/cats/Eukanuba_Top_Condition_7+_Senior.json')['Composition per 100g']
    diet_plan = WeightLossPlanner(animal, 10, dry, wet, 0.5, 0.5).plan_diet()
        
    """
    
    def __init__(
        self,
        animal,
        target_weight,
        dry_food_dict,
        wet_food_dict,
        proportion_dry,
        proportion_wet,
        per_week_loss_percentage=1.25,
        MER_factor=1.
    ):
        self.animal = animal
        self.target_weight = target_weight
        
        self.dry_food_dict = dry_food_dict
        self.wet_food_dict = wet_food_dict
        
        if proportion_dry + proportion_wet != 1.:
            raise ValueError('The sum of the proportion of dry and wet food should be equal to 1')
            
        self.proportion_dry = proportion_dry
        self.proportion_wet = proportion_wet
        
        if per_week_loss_percentage>2.0:
            warnings.warn("A loss of more than 2% of body weight per week"
                          "can cause serious health issue, check the correct"
                          "value for your animal with a veterinarian")          
        self.per_week_loss_percentage = per_week_loss_percentage
        self.MER_factor = MER_factor
        
    def get_weight_df(self):
        df = pd.DataFrame(columns=['Weight'])
        weigth_ = self.animal.weight
        date = datetime.now().date()
        while weigth_ > self.target_weight:
            df.loc[date,'Weight'] = weigth_
            weigth_ = weigth_ * ((100-self.per_week_loss_percentage)/100)
            date = date + timedelta(days=7)
        df.loc[date,'Weight'] = self.target_weight
        return df
    
    def plan_diet(self):
        df_weight = self.get_weight_df()
       
        _ME_wet = ME(
            self.wet_food_dict["Humidity (g)"]['total'],
            self.wet_food_dict["Protein (g)"]['total'],
            self.wet_food_dict["Fat (g)"]['total'],
            self.wet_food_dict["Ashes (g)"]['total'],
            self.wet_food_dict["Fibers (g)"]['total'],
            self.animal.species
         )
 
        _ME_dry = ME(
            self.dry_food_dict["Humidity (g)"]['total'],
            self.dry_food_dict["Protein (g)"]['total'],
            self.dry_food_dict["Fat (g)"]['total'],
            self.dry_food_dict["Ashes (g)"]['total'],
            self.dry_food_dict["Fibers (g)"]['total'],
            self.animal.species
         )
        for i, r in df_weight.iterrows():
            weight = r.values[0]
            _MER = np.ceil(MER(weight, self.MER_factor))
            quantity_wet = np.ceil(((_MER * self.proportion_wet)/_ME_wet)*100)
            quantity_dry = np.ceil(((_MER * self.proportion_dry)/_ME_dry)*100)
            df_weight.loc[i, 'Target kcal (ME)'] = _MER
            df_weight.loc[i, 'Wet food (g) / day'] = quantity_wet
            df_weight.loc[i, 'Dry food (g) / day'] = quantity_dry
            
        return df_weight


