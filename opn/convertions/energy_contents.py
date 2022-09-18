# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:02:41 2022

@author: antoi
"""



def RER(weight):
    """
    resting energy requirement (RER)
    """
    return 70 * (weight)**0.75 


def MER(weight, X):
    """
    Maintenance Energy Requirement (MER)
    
    Table 1: Maintenance Energy Requirement (MER) Factors
    (Canine,  Feline)
    Critical care/hospitalized : 1.0 * RER, 1.0 * RER
    Weight loss/obese : 1.0 * RER, 0.8-1.0 * RER
    Overweight-prone/inactive : 1.2-1.4 * RER, 1.0 * RER
    Neutered adult : 1.6 * RER, 1.2 * RER
    Intact adult : 1.8 * RER, 1.4 * RER
    Gestation : 1.6-2.0 * RER(1), 2-3 * RER(1)
    Lactation : 2-6 * RER, 2-6 * RER
    Growth (puppies/kittens) : 2-3 * RER(2), 2-3 * RER(2)
    
    
    1- depends on stage of gestation (cats steadily increase throughout gestation, while dogs remain relatively stable
    until the third trimester, at which point their energy needs increase)
    2 – puppies and kittens have higher energy needs when they are younger and they start decreasing around 4
    months of age until they are fully grown (which will vary with breed)
    
    """
    return RER(weight) * X


def ME2(moisture, protein, fat, ash, fiber):
    """
    Alternative formula for ME
    """
    _NFE = NFE(moisture, protein, fat, ash, fiber)
    return protein*3.5 + fat*8.5 + _NFE*3.5

def NFE(moisture, protein, fat, ash, fiber):
    """
    Nitrogen Free extract (g/100g)
    """
    return 100 - (moisture + protein + fat + ash + fiber)

def GE(moisture, protein, fat, ash, fiber):
    """
    Gross energy (kcal/100g)
    """
    _NFE = NFE(moisture, protein, fat, ash, fiber)
    return  (5.7 * protein) + (9.4 * fat) + (4.1 * (_NFE + fiber))

def Digestibility_cat(fiber, moisture):
    """
    % energy digestibility for cats
    """
    return 87.9 - ((0.88 * fiber * 100)/(100 - moisture))

def Digestibility_dog(fiber, moisture):
    """
    % energy digestibility for dogs
    """
    return  91.2 - ((1.43 * fiber * 100)/(100 - moisture))

def DE(moisture, protein, fat, ash, fiber, animal):
    """
    Digestible energy (kcal/100g)
    """
    if animal == 'cat':
        digestibility = Digestibility_cat(fiber, moisture)
    elif animal == 'dog':
        digestibility = Digestibility_dog(fiber, moisture)
    _GE = GE(moisture, protein, fat, ash, fiber)
    return _GE * (digestibility/100)

def ME(moisture, protein, fat, ash, fiber, animal):
    """
    Metabolizable energy (kcal/100g)
    """
    _DE = DE(moisture, protein, fat, ash, fiber, animal)
    if animal == 'cat':
        return _DE - (0.77 * protein)
    elif animal == 'dog':
        return _DE - (1.04 * protein)
     