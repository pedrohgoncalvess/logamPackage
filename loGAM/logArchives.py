from os import path
from typing import Dict
from types import FunctionType
import os
from .logConfig import loadConfig,logConfig


def createDirectory(func:FunctionType) -> FunctionType:
    dictConfigs = logConfig()
    pathLogging = dictConfigs['path']
    vali = path.exists(pathLogging+'\\Logs')
    if vali != True:
        os.mkdir(pathLogging+'\\Logs')
    else:
        pass

    def createArchiveFunction(dictConfigs):
        func(dictConfigs)
    return createArchiveFunction

@createDirectory
def createArchives(dictConfigs:Dict):
    pathLogging = dictConfigs['path']
    archives = dictConfigs['archives']
    for archive in archives:
        validation = path.exists(pathLogging+'\\Logs\\'+archive+'.txt')
        if validation != True:
            open(pathLogging+'\\Logs\\'+archive+'.txt','w')
        else:
            pass