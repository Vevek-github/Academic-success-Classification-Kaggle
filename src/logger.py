import os
import sys
import logger ,logging
from datetime import datetime

log_file = f"{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log"

log_path = os.path.join(os.getcwd(), "logs", log_file)

os.makedirs(log_path,exist_ok=True)

log_file_path = os.path.join(log_path,log_file)


FORMAT = '%(asctime)s %(lineno)d- %(name)s-%(levelname)s- %(message)s'
logging.basicConfig(
    filename=log_file_path,
    format=FORMAT,
    level=logging.INFO

)


if __name__== "__main__":
    logging.info("Logging Started in date_time format")