'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R 
@Last Modified: 2024-07-11 
@Title : program to reverse an array (first element becomes last).


'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

def reversing(arr):
    
    """
    Description: Function to reverse the elements in the array.
    Parameters:
        arr:the input list containg elemrents to reverse
    Returns:
        None: 
    """
    
    arr=np.array(arr)
    logger.info(f"The original array is : {arr}")
    reversed_arr=np.flip(arr)
    logger.info(f"The reversed array is : {reversed_arr}")

def main():
    arr=list(input("Enter the elements to be reversed: ").split(","))
    reversing(arr)

if __name__ == '__main__':
    main()
    