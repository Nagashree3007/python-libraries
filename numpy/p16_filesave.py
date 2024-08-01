'''


@Author: Nagashree C R
@Date: 2024-07-24 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11 
@Title :python program to add numpy array to textfile

'''
import loggingfile
import os
import numpy as np

fname = os.path.basename(__file__)
logger = loggingfile.logger_init(fname)

# Create a NumPy array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the filename
filename = 'array_data.txt'

# Save the array to a text file
np.savetxt(filename, array, fmt='%d', delimiter=',', header='Column1,Column2,Column3')

logger.info(f"Array saved to {filename}")
