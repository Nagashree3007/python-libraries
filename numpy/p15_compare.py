'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title :program compare two arrays using numpy.


'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

# Define the arrays
a = np.array([1, 2])
b = np.array([4, 5])

# Perform comparisons
greater_than = a > b
greater_than_or_equal = a >= b
less_than = a < b
less_than_or_equal = a <= b

# Print the results
logger.info("a > b")
logger.info(greater_than)

logger.info("a >= b")
logger.info(greater_than_or_equal)

logger.info("a < b")
logger.info(less_than)

logger.info("a <= b")
logger.info(less_than_or_equal)
