"""
This file contains all the code that is used
most commonly"""

import time
import datetime

def log_records (fun):
    def logging_records(*args, **kwargs):
        start_time = datetime.datetime.now()
        print(f"Running the function the function:{fun.__name__} at time {start_time}")
        result = fun(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f"Successfully executed the function:{fun.__name__} at time {end_time}")
        print(f"The total time taken is {end_time - start_time}")

        return result
    return logging_records
