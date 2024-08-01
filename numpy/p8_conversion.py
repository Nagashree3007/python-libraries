'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title : program to convert a list and tuple into arrays.


'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)


# List to array:
# [1 2 3 4 5 6 7 8]
# Tuple to array:
# [[8 4 6]
# [1 2 3]]



def input_val(val):
    if type(val)==list:
        arr=np.array(val)
        return arr
    else:
        arr=np.array(tuplex)
        arr=np.reshape(arr,(2,3))
        return arr

listx=[1,2,3,4,5,6,7,8]
tuplex=(8,4,6,1,2,3)

logger.info(input_val(listx))
logger.info(input_val(tuplex))
