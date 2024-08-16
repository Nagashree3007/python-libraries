'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-24 
@Title : Python program to suppresses the use of scientific notation for small
numbers in numpy array.

'''

import numpy as np
import os
import loggingfile

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)


def main():

    logger.info(" Inside main method ")

    original_array = np.array([1.6e-10, 1.6, 1200, 0.235])
    logger.info("Original array elements:")

    logger.debug(original_array)
    np.set_printoptions(suppress=True, precision=3)
    logger.debug(f" Array after {original_array}")
    

if __name__ == '__main__':
    main()