'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title :program to find the real and imaginary parts of an array of complex numbers.


'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

# Original array of complex numbers
original_array = np.array([1.00000000 + 0.j, 0.70710678 + 0.70710678j])

logger.info("Original array:", original_array)

# Real part of the array
real_part = np.real(original_array)
logger.info("\nReal part of the array:")
logger.info(real_part)

# Imaginary part of the array
imaginary_part = np.imag(original_array)
logger.info("\nImaginary part of the array:")
logger.info(imaginary_part)
