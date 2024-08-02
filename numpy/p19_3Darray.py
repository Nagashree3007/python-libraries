'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title : Python program to create a 3-D array with ones on a diagonal and zeros.

'''

import numpy as np
import os
import loggingfile

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)


def create_diagonal():
    
    """
    Description: Function to create a 3-D array with ones on a diagonal and zeros
                using inbult function called as eye function.
    Parameters:
        :
    Returns:
        None:
    """
    
    logger.info(" Inside 'create_diagonal' method ")
    diagonal_array = np.eye(3, dtype=int)*1
    logger.debug(f" Diagonal array\n {diagonal_array} ")


def main():

    logger.info(" Inside main method ")

    logger.info(" calling 'create_diagonal()' method ")
    create_diagonal()


if __name__ == '__main__':
    main()