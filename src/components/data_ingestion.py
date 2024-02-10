import os
import  sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass ## it is use to create class variable
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig, ModelTrainer

## in data ingestion component there should be some input that may be probably required by data ingestion 
# component input can be like whrere i have to save train data where i have to save test data ,where i have to 
#save the raw data those kind of input we basically creating in another class called  dataingestionconfig class


## input is given to the data  ingestion componenet then data ingestion component known where to save the train,
# test , data path becoause of this file path
@dataclass  ##decorator iside a class we define a class  variable we use __init__() but using data clas we can 
class DataIngestionConfig:  # directly define a class variable #create string path
    train_data_path: str=os.path.join('artifacts',"train.csv") #  this will be the default value of train_data_path
    #data will be ingested inside artifacts folder as file name train.csv same like
    test_data_path: str=os.path.join('artifacts',"test.csv")
    #raw data path
    raw_data_path:str = os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() ## initialise three path as soon as it is called the
        # three  path save inside particular class variable inside this variable threre may be subvariable
      
    def initiate_data_ingestion(self): ## write code here to read data from data base like mongodb, mysql
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info('Read the dataset as dataframe')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) # train_data_path>parameter // directory name //exist_ok if folder already there keep that
            
            logging.info("Train test split initiated")

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of the data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise logging.info(CustomException(e,sys))
            

if __name__=="__main__":
           obj=DataIngestion() #create a object of DataIngestion class
           train_data, test_data = obj.initiate_data_ingestion() ## from return of  function call assign value to two variables

           data_transformation = DataTransformation()  ## from importing from data_transformation
           train_arr,test_arr = data_transformation.initiate_data_transformation(train_data,test_data) ## provide train and test data 
           ## from data_ingestion to  this  methods of data_transformation as argument return train_arr , test_arr
           #which are use in model_trainer > ModelTrainer> initiate_model_trainer
           modeltrainer = ModelTrainer()
           print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
                    
## run in cmd :python -m src.components.data_ingestion
## or : python src/components/data_ingestion.py
