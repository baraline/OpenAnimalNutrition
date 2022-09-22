# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:03:09 2022

@author: antoi
"""

"""
- Nutrition Score
- Ingredient Score
- Compatibility Score (with specified animal)


"""
from abc import ABC, abstractmethod

class _FoodScorer(ABC):
    def __init__(
        self,
        animal,
        recommended_values,
    ):
        self.animal = animal
        self.recommended_values = recommended_values
    
    @abstractmethod
    def get_nutrition_score(self, food_dict):
        raise NotImplementedError()
    
    @abstractmethod
    def get_ingredient_score(self, food_dict):
        raise NotImplementedError()
    
    @abstractmethod
    def get_compatibility_score(self, food_dict):
        raise NotImplementedError()
    
    
class CatFoodScorer(_FoodScorer):
    def __init__(self, animal, recommended_values):
        super().__init__(animal, recommended_values)