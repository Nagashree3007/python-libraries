'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title : program to create 3x3 matrix with values ranging from 2 to 10.


'''

import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

def matrix(start,end):
    matrix=np.arange(start,end).reshape(3,3)
    return matrix
    
def main():
    S,E=map(int,input("enter the start and end of digits of matrix").split(","))
    logger.debug(matrix(S,E))
    
if __name__=="__main__":
    main()