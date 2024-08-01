'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title :Python program to add a border (filled with 0's) around an existing array.

'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)


def add_border(arr):
    # Determine the shape of the new array
    original_shape = arr.shape
    new_shape = (original_shape[0] + 2, original_shape[1] + 2)
    
    # Create a new array with zeros
    bordered_arr = np.zeros(new_shape, dtype=arr.dtype)
    
    # Copy the original array into the new array, offset by 1
    bordered_arr[1:-1, 1:-1] = arr
    
    return bordered_arr



ele=list(map(float,input("enter the elemts of thr matrix : ").split(',')))
r,c=input("enter number of rows and coloums").split(',')
r=int(r)
c=int(r)
# Define the original array
original_array = np.array(ele, dtype=float).reshape(r,c)

# Add the border
new_array = add_border(original_array)

# Print the results
logger.info("Original array:")
logger.info(original_array)
logger.info("\nArray with border:")
logger.info(new_array)
