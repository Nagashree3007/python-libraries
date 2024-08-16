'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title : program to find the number of elements of an array, length of one
array element in bytes and total bytes consumed by the elements.

'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

array=list(map(int,input("enter the array elements:").split(",")))
array = np.array(array)

# Calculate the number of elements
num_elements = array.size

# Calculate the size of one element in bytes
size_of_one_element = array.itemsize

# Calculate the total bytes consumed by the elements of the array
total_bytes = num_elements * size_of_one_element

# Output the results
logger.info(f"Size of the array: {num_elements}")
logger.info(f"Length of one array element in bytes: {size_of_one_element}")
logger.info(f"Total bytes consumed by the elements of the array: {total_bytes}")