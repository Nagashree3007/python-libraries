'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title :Python program to create a 2d array with 1 on the border and 0 inside.


'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

f=[1. for i in range (1,26)]
arr=np.array(f)
x=np.reshape(arr,(5,5))
x[1:4,1:4]=0.
logger.info(x)