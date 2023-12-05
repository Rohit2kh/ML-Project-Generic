import sys
from src.logger import logging

#getting the details , line number , and filename in which exception is occured
def display_error_message(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"


    return error_msg


#custom exception class

class Custom_exception(Exception):
    def __init__(self, error_msg, error_details:sys):
        super().__init__(error_msg)#override the init method of exception class in custom exception class
        self.error_msg = display_error_message(error=error_msg, error_details=error_details)

    def __str__(self):#print the exceptions
        return self.error_msg
    


# if __name__=="__main__":

#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise Custom_exception(e,sys)
    
