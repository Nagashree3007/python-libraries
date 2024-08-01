'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title : program to convert a list of numeric value into a one-dimensional NumPy array.


'''

import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)


def original(original_list):
    
    # Convert the list to a NumPy array
    numpy_array = np.array(original_list)
    # Print the original list and the NumPy array
    logger.debug(f"Original List: {original_list}")
    logger.debug(f"One-dimensional numpy array:{numpy_array}")

# Original list of numeric values
#given original_list = [12.23, 13.32, 100, 36.32]    


def main():
    original_list=list(input("enter original list").split(','))
    original(original_list)
    
if __name__=="__main__":
    main()