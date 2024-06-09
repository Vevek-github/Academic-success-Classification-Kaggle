import sys
import os

# Find the directory containing the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Move up two levels to the main folder
main_folder = os.path.dirname(current_dir)
# Add the main folder to the Python path
sys.path.append(main_folder)

# Now you can import pipeline_exception.py
from..exception import CustomException




import pandas as pd
from logger import logging
from exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass                                                          # Decorator  
class data_ingestion_config():
    train_data_path = os.path.join("Artifacts","train_data.csv")
    test_data_path = os.path.join("Artifacts","test_data.csv")
    raw_data_path = os.path.join("Artifacts","raw_data.csv")


class data_ingestion():

    def __init__(self):                                                                     # Constructor
        self.ingestion_config = data_ingestion_config()
    
    def initiate_data_ingestion(self):
        try :
            data = pd.read_csv(os.path.join("Data","train.csv"))                            # Currently pulling data from local machine 
            logging.info("Data Ingested into the Machine.")                                  # can use kaggle api to pull data 

            os.makedirs(os.path.join(os.path.dirname(self.ingestion_config.raw_data_path)))
            data.to_csv(os.path.join(self.ingestion_config.raw_data_path),index=False)
            test_size = 0.2
            logging.info(f"Raw data has split into train and test with test_size of {test_size} ")
            train_set , test_set = train_test_split(data, test_size=test_size,random_state=44)
            train_set.to_csv(os.path.join(self.ingestion_config.train_data_path),index=False)
            test_set.to_csv(os.path.join(self.ingestion_config.test_data_path),index=False)
        
            return (self.ingestion_config.train_data_path 
                    ,self.ingestion_config.test_data_path
                    )
        
        except Exception as e :
            excep = CustomException(e,sys)
            logging.info(f"{excep.error_message(e,sys)}")
            raise CustomException(e,sys)



if __name__ == "__main__":
    obj = data_ingestion()