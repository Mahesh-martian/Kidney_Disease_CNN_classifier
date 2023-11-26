import os
from box.exceptions import BoxValueError
import yaml
from KidneyCnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path):
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(name=path, exist_ok=True)
        
        if verbose:
            logger.info(f"created directory at: {path}")
            

@ensure_annotations
def save_json(path: Path, data:dict):
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved to: {path}")
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file from given path

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data  as class attribute instead of dict
    """    
    with open(path, 'r') as f:
        content = json.load(f)
        
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~ {size_in_kb} KB'
