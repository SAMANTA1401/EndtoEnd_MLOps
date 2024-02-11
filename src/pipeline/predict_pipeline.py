## here prediction part is created

import sys 
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
from src.logger import logging

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self, features): ##  method to make predictions on the test data
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path ='artifacts\preprocessor.pkl'  ## handle feature scaling , categorical handle
            print('bofore loading')
            model = load_object(file_path=model_path) #calling load object from utils funtion import pickle and load the pickle file 
            preprocessor = load_object(file_path=preprocessor_path)
            print('after loading')
            data_scaled=preprocessor.transform(features) ##The fit-transform method is calculating the mean and 
            #variance of each of the features present in our data. The transform method is\
            #  transforming all the features using the respective mean and variance.
            preds = model.predict(data_scaled) #prediction on scaled data using load model
            return preds
        except  Exception as e:
            raise logging.info(CustomException(e,sys))


class CustomData:   ## this class mapping the input data from html to the backend
    def __init__(self,
        gender:str,
        race_ethnicity:str,
        parental_level_of_education:str,
        lunch:str,
        test_preparation_course:str,
        reading_score:int,
        writing_score:int):

        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self): ## this function return all inputs as dataframe
        try:
            custom_data_input_dict = {
                "gender":[self.gender],
                "race/ethnicity":[self.race_ethnicity],
                "parental level of education":[self.parental_level_of_education] ,
                "lunch": [self.lunch],
                "test preparation course":[self.test_preparation_course],
                'reading score':[self.reading_score],
                'writing score':[self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise logging.info(CustomException(e,sys))

