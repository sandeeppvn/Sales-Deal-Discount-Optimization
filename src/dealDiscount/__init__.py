import os
import sys
import logging

logging_format = '[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'

log_dir = os.path.join(os.path.dirname(__file__), 'logs')
log_file = os.path.join(log_dir, 'logs.txt')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("dealDiscount")