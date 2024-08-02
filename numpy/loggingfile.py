import logging

# def mylogging(filename):
    
#     logging.basicConfig(filename='log.txt',filemode='w',level=logging.DEBUG, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
#     logging.basicConfig(filename='log.txt', level=logging.INFO, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
#     logging.basicConfig(filename='log.txt', level=logging.WARNING, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
#     logging.basicConfig(filename='log.txt', level=logging.ERROR, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
#     logging.basicConfig(filename='log.txt', level=logging.CRITICAL, format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s")

#     return logging.getLogger(__name__)




def logger_init(name):
    logger = logging.getLogger(name)
    # configuring our specific logger
    # setting the log level for the logger
    logger.setLevel(logging.DEBUG)
    # creating a formatter
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler('numpy.log')
    # adding the formatting to the file handler
    file_handler.setFormatter(formatter)
    # to display the result in the console
    stream_handler = logging.StreamHandler()
    # adding the formatting to the stream handler
    stream_handler.setFormatter(formatter)
    # adding file handler and stream_handler to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
