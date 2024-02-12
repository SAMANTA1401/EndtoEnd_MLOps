# it is a clone of app.py file for deployment purpose

## it is use for flask web app
from flask import Flask ,request,render_template, url_for, redirect
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask( __name__)  # creating the object of class Flask this application present in  .ebextensions
## python.config to tell aws beanstalk about starting point of application

app = application

##creating for a home page

@app.route('/')     #home page route
def index():
    return render_template('index.html')   #returning html file in templates folder to our homepage

# @app.route('/predictdata')
# def predict_Data():
#     return render_template('home.html') ## input data field


@app.route('/predictdata', methods=['GET','POST'])   #for prediction
def predict_datapoint():
    if request.method =='GET':
        return render_template('home.html') ## input data field
    else:
        data = CustomData(  #this function will created and send data to src> pipeline >predict 
            # pipeline create objectt customdata class
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get("ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=float(request.form.get("reading_score")),
            writing_score=float(request.form.get('writing_score'))            
        )     
        pred_df = data.get_data_as_data_frame() # data convert to dataframe in predict pipeline retireve as pred_df
        print(pred_df)
        print('before prediction')

        predict_pipeline = PredictPipeline() ## create  an object of predictPipeline in predicct_pipeline.py
        results = predict_pipeline.predict(pred_df)  ##call predict function under Predictpipeline class

        return render_template('home.html', results=results[0]) ## it is basically a list format give output in home.html
        # inplace of results


if __name__=='__main__':

    app.run() # remove debug =true for deployment
