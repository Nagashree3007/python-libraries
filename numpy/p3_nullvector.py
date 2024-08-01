'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title : create a null vector of size 10 and update sixth value to 11.


'''

import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

def createNullVector(size,index,update_value):
    
    """
    Description: Function to create null vector with given size and updating the specified index value with specified value.
    Parameters:
        size: Function taking size for null vector creation.
        index: Function taking index for update the exsisting value in given index.
        update_value: Function taking value which is replaced by given value at specified index.
    Returns:
        None: 
    """
    
    logger.debug("Inside null vector method")

    null_vector = np.zeros(size)
    logger.debug(f"original vector: {null_vector}")

    null_vector[index]=update_value
    logger.debug(f"Updated null vector: {null_vector}")
    
    logger.debug(f"Null vector index {index} is updated to {update_value}")

def main():
    
    size = 10
    index = 6
    update_value = 11
    createNullVector(size,index,update_value)


if __name__ == '__main__':
    main()
    