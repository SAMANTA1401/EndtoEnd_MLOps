import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y__%H_%M_%S')}.log" #create log file, it is a text file
##02_05_2024__00_25_10.log
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE)  ## give a path  to the logs file join current working 
##D:\a27_YEARS_OLD\EndtoEnd_MLOps\logs\02_05_2024__00_25_10.log
## directory with 'logs' and filename from above logfile
os.makedirs(logs_path,exist_ok=True)  ## make directories or create folder of log path if though there is a file keep  
#adding new files in this folder
#D:\a27_YEARS_OLD\EndtoEnd_MLOps\logs\02_05_2024__00_25_10.log
##D:\a27_YEARS_OLD\EndtoEnd_MLOps\   {"logs\02_05_2024__00_25_10.log"}=>(log directory or log folder)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) ##path to  existing log file or creating one if not exist
#D:\a27_YEARS_OLD\EndtoEnd_MLOps\logs\02_05_2024__00_25_10.log\02_05_2024__00_25_10.log
####D:\a27_YEARS_OLD\EndtoEnd_MLOps\<logs\02_05_2024__00_25_10.log\>(log folder) <02_05_2024__00_25_10.log>(log file)

logging.basicConfig(
    filename=LOG_FILE_PATH, ##print log message in this directory 
    format="[ %(asctime)s ] %(lineno)d %(name)s  - %(levelname)s : %(message)s ", ##print message format
    level=logging.INFO #print specific message only %(levelname)s
)
##format > [ 2024-02-05 00:25:10,033 ] 21 root  - INFO : logging has started 

# if __name__=="__main__":  ##When run as a script-True to check esecuting purpose loger.py,  not as a imported module -False from another  scripts

#     logging.info("logging has started") ##%(message)s