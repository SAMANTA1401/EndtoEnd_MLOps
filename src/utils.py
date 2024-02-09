## utils has all the common things that we are going to  import and use commmon functionality
#  the entire project can use  this module.
import os
import sys
import dill ## help to create pickle file

import numpy as np    
import pandas as pd

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj) ###we will be using the dump() and load() functions
            # to pickle Python objects to a file and unpickle them

    except Exception as e:
        raise logging.info(CustomException(e,sys))