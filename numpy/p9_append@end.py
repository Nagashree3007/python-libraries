'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title :program to append values to the end of an array.


'''
import loggingfile
import os
import numpy as np 

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

arr=[10,20,30]
arr=np.array(arr)
f=[i*10 for i in range(4,11)]
new_arr=np.array(f)
arr=np.concatenate((arr,new_arr))
logger.info(arr)