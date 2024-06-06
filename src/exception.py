#  How we use it ... say a = CustomException(e,sys)   then logging.info(a.error_message)    FOR CAPTURING THE ERROR 

import os , sys
from logger import logging

def detailed_error_msg(error,error_detailed:sys)->str:
    _ ,_ , exc_tb = error_detailed.exc_info()

    filename = exc_tb.tb_frame.f_code.co_filename 

    error_message = "Error occured in file_Name  : [{0}] in line_number : [{1}] with error as [{2}] ".format(filename,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, e,sys ):
        #super.__init__()
        self.error_message =  detailed_error_msg(e,sys)
        

    def __str__(self) -> str:
        return self.error_message
    
if __name__ == "__main__":
    try :
        pass
        #a= 1/0
    except Exception as e :
        logging.info("Divided by zero .....Starting ")
        raise CustomException(e,sys)



