# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 22:45:38 2022

@author: antoi
"""

def _validate_species_str(s):
    #TODO
    return s

class Animal:
    def __init__(
        self,
        species,
        weight,
        age,
        is_neutered,
        is_active,
        health_condition=None
    ):
        self.species = _validate_species_str(species)
        self.weight = weight
        self.age = age
        self.is_neutered = is_neutered
        self.is_active = is_active
        self.health_condition = health_condition
    

        
        
    
    
        