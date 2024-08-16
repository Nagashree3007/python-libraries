'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title :program to find common values between two arrays.


'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

arr1=list(map(int,input("enter the array1 elements:").split(",")))
# Array1=[ 0,10, 20 ,40 ,60]
# Array2= [10, 30, 40,]
arr2=list(map(int,input("enter the array2 elements:").split(",")))
arr1=np.array(arr1)
arr2=np.array(arr2)

intersection = np.intersect1d(arr1, arr2)

logger.info(f"the common elements in two arrays are:{intersection}")