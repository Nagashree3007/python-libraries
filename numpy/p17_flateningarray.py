'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title :program to create a contiguous flattened array.


'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

# [[10 20 30]
# [20 40 50]]
# New flattened array:
# [10 20 30 20 40 50]
a=np.array([[10,20,30],[20,40,50]])
x=a.flatten()
logger.info(x)