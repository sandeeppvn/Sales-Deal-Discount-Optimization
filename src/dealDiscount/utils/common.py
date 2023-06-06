import os
from box.exceptions import BoxValueError
import yaml
from dealDiscount import logger
import json
import joblib
from ensure import ensure_annotations
from typing import Any
from box import ConfigBox
from pathlib import Path

@ensure_annotations
def read_yaml_file(file_name: Path) -> ConfigBox:
    """Read yaml file and return a ConfigBox object
    
    Args:
        file_name (Path): Path to yaml file

    Raises:
        BoxValueError: If yaml file is not valid
        e: empty file

    Returns:
        ConfigBox: ConfigBox object
    """
    try:
        with open(file_name, 'r') as yaml_file:
            yaml_config = yaml.safe_load(yaml_file)  
            logger.info(f"Reading yaml file: {file_name}")
            config = ConfigBox(yaml_config)
            return config
    except BoxValueError:
        logger.error(f"yaml file is empty: {file_name}")
        raise ValueError(f"yaml file is empty: {file_name}")
    except Exception as e:
        logger.error(f"Error reading yaml file: {file_name}")
        raise e
    
@ensure_annotations
def create_directories(dirs: list):
    """Create directories if they don't exist
    
    Args:
        dirs (list): List of directory paths
    """
    for dir_path in dirs:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            logger.info(f"Created directory: {dir_path}")

@ensure_annotations
def save_json_file(file_name: Path, data: dict):
    """Save json data
    
    Args:
        file_name (Path): Path to json file
        data (dict): Data to save
    """
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"Saved json file: {file_name}")

@ensure_annotations
def load_json_file(file_name: Path) -> ConfigBox:
    """Load json file
    
    Args:
        file_name (Path): Path to json file

    Returns:
        ConfigBox: ConfigBox object
    """
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
        logger.info(f"Loaded json file: {file_name}")
        return ConfigBox(data)
