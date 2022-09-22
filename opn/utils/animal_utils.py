# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 22:45:38 2022

@author: antoi
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(
        self,
        weight,
        age,
        is_neutered,
        is_active,
        health_condition=None
    ):
        self.weight = weight
        self.age = age
        self.is_neutered = is_neutered
        self.is_active = is_active
        self.health_condition = health_condition
        super().__init__()
        
    @abstractmethod
    def estimate_MER_factor(self):
        """
        Table 1: Maintenance Energy Requirement (MER) Factors
        (Canine,  Feline)
        Critical care/hospitalized : 1.0 * RER, 1.0 * RER
        Overweight-prone/inactive : 1.2-1.4 * RER, 1.0 * RER
        Neutered adult : 1.6 * RER, 1.2 * RER
        Intact adult : 1.8 * RER, 1.4 * RER
        Gestation : 1.6-2.0 * RER(1), 2-3 * RER(1)
        Lactation : 2-6 * RER, 2-6 * RER
        Growth (puppies/kittens) : 2-3 * RER(2), 2-3 * RER(2)
        """
        raise NotImplementedError()
        
    @abstractmethod
    def estimate_MER_factor_weight_loss(self):
        """
        Table 1: Maintenance Energy Requirement (MER) Factors
        (Canine,  Feline)
        Weight loss/obese : 1.0 * RER, 0.8-1.0 * RER
        """
        raise NotImplementedError()

class Dog(Animal):
    def __init__(
        self,
        weight,
        age,
        is_neutered,
        is_active,
        health_condition=None
    ):
        super().__init__(
            weight,
            age,
            is_neutered,
            is_active,
            health_condition=health_condition
        )
        self._str = 'dog'
    

    def estimate_MER_factor(self):
        if self.age < 0.5:
            return 2.5
        if self.is_active and not self.is_neutered:
            return 1.8
        if self.is_active and self.is_neutered:
            return 1.6
        if not self.is_active:
            return 1.3
        raise ValueError('The characteristics of the animal do not yet allow an automatic estimation of the MER factor.')
        
    def estimate_MER_factor_weight_loss(self):
        if self.is_active and not self.is_neutered:
            return 1.
        if self.is_active and self.is_neutered:
            return 1.
        if not self.is_active:
            return 1.

class Cat(Animal):
    def __init__(
        self,
        weight,
        age,
        is_neutered,
        is_active,
        health_condition=None
    ):
        super().__init__(
            weight,
            age,
            is_neutered,
            is_active,
            health_condition=health_condition
        )
        self._str = 'cat'
    
    def estimate_MER_factor_weight_loss(self):
        if self.is_active and not self.is_neutered:
            return 1
        if self.is_active and self.is_neutered:
            return 0.975
        if not self.is_active:
            return 0.95
        
    def estimate_MER_factor(self):
        if self.age < 0.5:
            return 2.5
        if self.is_active and not self.is_neutered:
            return 1.4
        if self.is_active and self.is_neutered:
            return 1.2
        if not self.is_active:
            return 1.0
        raise ValueError('The characteristics of the animal do not yet allow an automatic estimation of the MER factor.')
        