##  To do feature engeneering ,data cleaning, convert data set categorical to numerical, missing values

import sys
import pandas as pd
import numpy as np
from sklearn.compose import  ColumnTransformer ## to create pipleline
from sklearn.impute import SimpleImputer ##responsible to  handle the missing value in dataset
from sklearn.pipeline import  Pipeline  ##A sequence of data transformers with an optional final predictor.
#Pipeline allows you to sequentially apply a list of transformers to preprocess the data and, if desired,
#  conclude the sequence with a final predictor for predictive modeling.
#ntermediate steps of the pipeline must be ‘transforms’, that is, they must implement 
# fit and transform methods. The final estimator only needs to implement fit. The transformers in the 
# pipeline can be cached using memory argument.
from  sklearn.preprocessing import OneHotEncoder , StandardScaler
from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object 
from dataclasses import dataclass

@dataclass
class DataTransformationConfig: # class to hold path configuration for data transformation 
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")  ##Pickle can be used to serialize 
    #and deserialize objects. A seralized object can be saved and loaded from the disk. Pickling is a
    #  method to convert an object (list, dict, etc) to a file and vice versa

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        ''' This function is responsible for data transformation '''
        try :
            numerical_features = ['reading score', 'writing score'] #'math score',
            categorical_features = [
                'gender', 
                'race/ethnicity', 
                'parental level of education', 
                'lunch', 
                'test preparation course'
            ]
            num_pipeline=Pipeline( ## this pipeline run on the training dataset like fit transform
                steps=[
                    ('imputer',SimpleImputer(strategy="median")), #to avoid outlairs and replace missing vlues with median
                    ("scaler", StandardScaler())  ##
                ]
            )
            logging.info("Numerical  columns standard scaling completed")
           


            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy= "most_frequent")), ##Univariate imputer for completing missing 
                    # values with simple strategies.
                    # Replace missing values using a descriptive statistic (e.g. mean, median, or most frequent)
                    #  along each column, or using a constant value.
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info("Categorical columns encoding completed")

            logging.info(f"Categorical features: {categorical_features}")
            logging.info(f"Numerical features: {numerical_features}")

            preprocessor =ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_features),
                    ("cat_pipelines",cat_pipeline,categorical_features)
                ]
            )

            return preprocessor

        except  Exception as e:
            raise logging.info(CustomException(e,sys))
        


    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("obtaining preprocessing object")

            preprocessor_obj = self.get_data_transformer_object()

            target_column_name = 'math score'
            numerical_features = ['reading score', 'writing score']

            logging.info("read columns")

            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.fit_transform(input_feature_test_df)

            train_arr = np.c_[  ##A short technique for concatenation of arrays using numpy is np.c_ 
            #and np.r_ np.c_[] concatenates arrays along second axis but, np.r_[] concatenates arrays 
            # along first axis.
                input_feature_train_arr,np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing onbject. ")

            save_object(  ## funciton present inside the utils.py
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise logging.info(CustomException(e,sys))
                
        
    

