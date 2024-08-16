'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title : program to find the set difference of two arrays.


'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

arr1=list(map(int,input("enter the array1 elements:").split(",")))

arr2=list(map(int,input("enter the array2 elements:").split(",")))

# Array1=[ 0,10, 20 ,40 ,60]
# Array2= [10, 30, 40,]

arr1=np.array(arr1)
arr2=np.array(arr2)

intersection = np.intersect1d(arr1, arr2)
x = [element not in intersection for element in arr1]
y=[element not in intersection for element in arr2]

z=np.concatenate((arr1[x],arr2[y]))
logger.info(f"the Set difference between two arrays:{z}")
# print(intersection)