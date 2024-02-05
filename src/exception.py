import sys
import logger

def error_message_detail(error,error_detail:sys): ##error details basically present inside the sys
    _,_,exc_tb=error_detail.exc_info()     # esecution info give three important information last info esc_tb
    ## provide which file ,in whicch line exeption has occured
    file_name=exc_tb.tb_frame.f_code.co_filename    ## vairable>properties inside>property.filename 
    ##from custom exception handling python documentation
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno, str(error)
    )  ## place holder value 0,1,2
    ###CustomException: Error occured in python script name [d:\a27_YEARS_OLD\EndtoEnd_MLOps\src\exception.py] 
     # line number [26] error message[division by zero]
    return  error_message                          ## returning formatted string to main function

class CustomException(Exception): ##The built-in exception classes can be subclassed to define new exceptions;
    #programmers are encouraged to derive new exceptions from the Exception class or one of its subclasses,
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)  #for Exception parent  class initialisation inbuilt from sys exec_info()
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message  ##whenever we try to print or execute we get erorr message
        ###CustomException: Error occured in python script name [d:\a27_YEARS_OLD\EndtoEnd_MLOps\src\exception.py] 
        # line number [26] error message[division by zero]


# if __name__=="__main__":  #to check executing this  exeption.py
#     try :
#         a=1/0
#     except Exception as e:
#         logger.logging.info(CustomException(e,sys)) ##print or log custom exception in logger file
#         raise CustomException(e,sys) #passing parameter

        ##CustomException: Error occured in python script name [d:\a27_YEARS_OLD\EndtoEnd_MLOps\src\exception.py] 
        # line number [26] error message[division by zero]
