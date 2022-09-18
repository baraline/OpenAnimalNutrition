# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 22:33:39 2022

@author: antoi
"""
import json
import jsonschema
from jsonschema import validate

def read_json(path):
    with open(path) as f:
        data = json.load(f)
    return data
        
        
def validateJsonFormat_Recommended_values(jsonData):
    Schema = read_json('~/input_data/recommended_values/base_format.json')
    try:
        validate(instance=jsonData, schema=Schema)
    except jsonschema.exceptions.ValidationError as err:
        return err
    return True