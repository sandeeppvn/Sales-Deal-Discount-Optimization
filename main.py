from dealDiscount import logger
from dealDiscount.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "STAGE 1: DATA INGESTION"
try:
    logger.info(f"Starting {STAGE_NAME}")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.run()
    logger.info(f"Completed {STAGE_NAME}")

except Exception as e:
    logger.error(e)
    raise e
