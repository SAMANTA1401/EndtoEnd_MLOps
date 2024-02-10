##model trainer module

import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression , Lasso ,Ridge
from sklearn.metrics import r2_score
from sklearn.neighbors import  KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    """Data class for model training configuration"""
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig() ## inside this variable  we will get the path trained_model_file_path

    def initiate_model_trainer(self,train_array,test_array): ## train array and test array getting from 
        # return of initate data transformation function  of data_transformation
        try:
            logging.info("split trainning and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "Linear Regression" : LinearRegression(),
                # "Lasso ": Lasso(),
                # "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "Gradient Boosting": GradientBoostingRegressor()

            }
            ## create a dictionary
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models) ## evaluate function present in utils

            ## to get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## to get best modal name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model =models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")

            logging.info(f"Best model is {best_model_name} with score {best_model_score}")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_sco = r2_score(y_test,predicted)

            return r2_sco
        


        except Exception as e:
            raise logging.info(CustomException(e,sys))
            


