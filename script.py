import logging
import os
import sys

import pymysql

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logging.info("Hello world")
logging.info(os.environ['TEST_SECRET'])

db_config = os.environ['RDS_CONFIG']
if db_config:
    logging.info("Got rds config")
else:
    logging.info("Rds config empty. Exiting.")
    sys.exit()

try:
    conn = pymysql.connect(db_config['host'], user=db_config['username'], passwd=db_config['password'], db=db_config['dbname'], connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded.")
