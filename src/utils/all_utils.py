import yaml
import os
import json

def read_yaml(path_to_yaml:str)-> dict:
    with open(path_to_yaml) as yaml_file:
        content=yaml.save_load(yaml_file)
    return content