# Pipeline step 1: Data Ingestion

from dealDiscount.config.configuration import ConfigurationManager
from dealDiscount.components.data_ingestion import DataIngestion
from dealDiscount import logger




class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def run(self):        
        config_mgr = ConfigurationManager()
        data_ingestion_config = config_mgr.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()


if __name__ == "__main__":
    try:
        STAGE_NAME = "STAGE 1: DATA INGESTION"
        logger.info(f"Starting {STAGE_NAME}")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.run()
        logger.info(f"Completed {STAGE_NAME}")
    except Exception as e:
        logger.error(e)
        raise e
    

