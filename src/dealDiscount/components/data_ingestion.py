import os
import urllib.request as request
from dealDiscount import logger
from dealDiscount.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if os.path.exists(self.config.local_data_file):
            logger.info(f"Data already exists at {self.config.local_data_file}")
            return
        
        logger.info(f"Downloading data from {self.config.source_url}")
        request.urlretrieve(self.config.source_url, self.config.local_data_file)
        logger.info(f"Data downloaded at {self.config.local_data_file}")