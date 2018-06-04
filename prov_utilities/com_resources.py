''' Module containing the settings for logger, formatter and app_num handler. '''

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('provLock.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

appNum_handler = logging.FileHandler('ApplicationRuning.log','w')
appNum_handler.setLevel(logging.ERROR)
appNum_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(appNum_handler)