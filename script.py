import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logging.info("Hello world")
logging.info(os.environ['TEST_SECRET'])