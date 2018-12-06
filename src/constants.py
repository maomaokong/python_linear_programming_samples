import os
import json


class Config:
    """
    Read default configurations from setting file
    """
    PATH_PARENT = os.path.dirname(os.getcwd())

    config_file = '{pp}/config.json'.format(pp=PATH_PARENT)

    with open(config_file, 'r') as cf:
        config = json.load(cf)

        APP_NAME = config['APP_NAME']
        VERSION = config['VERSION']
        ENV = config['ENV']

        PATH_SRC = config['PATHS']['SOURCE_CODE']
        PATH_DATA = config['PATHS']['DATA']
        PATH_LOG = config['PATHS']['LOG']
        PATH_TEST = config['PATHS']['TEST']


class Environment:
    """
    Application Environment Value
    """
    UAT = 1
    PROD = 9
