import configparser
import os

def get_config():
    config = configparser.ConfigParser()
    config.read(os.getcwd()+"\\utilities\\properties.ini")
    return config