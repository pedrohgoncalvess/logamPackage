from typing import Dict
from os import path
from colorsFont import colors

def loadConfig() -> str | Dict:
    with open('logConfig','r') as log:
        configs = log.read()
        preferences = configs.find('[preferences]')
        if preferences > -1:
            preferences = True
        else:
            preferences = False
            print(colors('cyan') + "Not found [preferences] in logConfig, read documentation for more flexible")
        configs = configs.replace(' ', '')
        configs = configs.split('\n')
        dictConfigs = {}
        for i in configs:
            listConfigs = i.split('=')
            if len(listConfigs) > 1:
                key = listConfigs[0]
                if key == 'archives' or key == 'levels' or key == 'log_format' or key == 'events':
                    value = listConfigs[1].split(',')
                else:
                    value = listConfigs[1]
                dictConfigAppend = {key:value}
                dictConfigs.update(dictConfigAppend)

    return preferences,dictConfigs


def logConfig():
    preferences,dictConfigs = loadConfig()
    dictLogging = {}
    try:
        pathLogging = dictConfigs['path']
        if path.exists(pathLogging) != True:
            print(colors('red') + f"{pathLogging} not exists.")
            exit()
        archives = dictConfigs['archives']
        pathLogging = {'path':pathLogging}
        archives = {'archives':archives}
        dictLogging.update(pathLogging)
        dictLogging.update(archives)
    except KeyError as config:
        print(f"{config} not found in logConfig")
        exit()
    if preferences == True:
        defaultValues = defaultConfigs()
        for configs in list(defaultValues.keys()):
            try:
                vars()[configs] = dictConfigs[configs]
            except:
                vars()[configs] = defaultValues[configs]
            vars()[configs] = {configs:vars()[configs]}
            dictLogging.update(vars()[configs])
    else:
        dictLogging = defaultConfigs()

    defaultConfigsSet = {'default_level': 'levels' , 'default_archive':'archives' , 'default_event':'events'}
    for default in list(defaultConfigsSet.keys()):
        try:
            dictLogging[default]
        except:
            dictLogging.update({default:dictLogging[defaultConfigsSet[default]][0]})

    return dictLogging

def defaultConfigs() -> Dict:
    dictLogging = {'levels': ['INFO', 'WARN', 'TRACE', 'ERROR', 'FATAL'], 'length_message': 'NO_LIMIT', 'date_format': None,
                   'log_format': ['time', 'method', 'level', 'message'],
                   'sep': ',','events':'log'}

    return dictLogging

logConfig()