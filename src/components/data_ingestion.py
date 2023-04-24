import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#create the required paths for train, test, raw data
@dataclass
class DataIngestionConfig:
    train_data_path: str= os.path.join('artifacts', "train.csv")
    test_data_path: str= os.path.join('artifacts',"test.csv")
    raw_data_path: str= os.path.join('artifacts',"data.csv")

#create the main class to perform operation
class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or components. ")
        try:
            df=pd.read_csv("notebook\data\stud.csv") #read data from like MongoDB , hadoop, API etc.
            logging.info("Read the dataset as dataframe")

            #create the artifacts folder 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            #save the copy of data as raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info ("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2, random_state=42)
            
            #save the train and test data into the respective file like  ('artifacts/train.csv')
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of data is completed. ")

            return (
                self.ingestion_config.test_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
       obj = DataIngestion()     
       obj.initiate_data_ingestion()
    