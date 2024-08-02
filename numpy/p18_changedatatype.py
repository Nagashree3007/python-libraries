'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-24 
@Title : Python program to change the data type of an array.

'''

import numpy as np
import os
import loggingfile

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)


def change_data_type(arr,data_type):
    
    """
    Description: Function to change array data type to specified data type.
    Parameters:
        arr: Function taking array as parameter
        data_type: Function taking the data type for converting the array into specified data type.
    Returns:
        None:
    """
    
    change_data_type = np.array(arr,dtype=data_type)

    logger.debug(f" Array with specified data type\n {change_data_type}")
    logger.debug(f" Array datatype is changed to  {change_data_type.dtype} ")


def main():

    logger.info(" Inside main method ")

    arr = np.array([[2,4,6],[8,5,6]],dtype='int32')
    data_type = 'float64'
    
    logger.debug(f" given array \n{arr} ")
    logger.debug(f" given array data type is {arr.dtype}")
    logger.debug(f" required to change array data type into {data_type} ")
    change_data_type(arr,data_type)


if __name__ == '__main__':
    main()