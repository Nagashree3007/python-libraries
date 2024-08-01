'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title : create a 8x8 matrix and fill it with a checkerboard pattern.


'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

arr=np.zeros((8,8))
for idx,x in np.ndenumerate(arr):
    if idx[0] % 2 != 0 and idx[1] % 2 != 0:
        arr[idx] = 1
    elif idx[0] % 2 == 0 and idx[1] % 2 == 0:
        arr[idx] = 1
logger.info(arr)