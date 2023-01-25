from os import path
from datetime import datetime
from typing import Dict
from types import FunctionType
import os
from logConfig import loadConfig

def dateFormat(configsLogging:Dict) -> str:
    try:
        date_format = configsLogging['date_format']
    except:
        date_format = None
    if date_format == None:
        date = datetime.now()
    else:
        now = datetime.now()
        date = str(now.strftime(date_format))
    return date

def checkLevel(configsLogging:Dict) -> str:
    pass




def writeLog(message:str,):
    pass


