import sys
import logging
from src.logger import logging

# Function to get detailed error message
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback details
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename
    error_message = "Error occurred in python script name [{0}] line no [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # Initialize the base Exception class
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message


