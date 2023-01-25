from loGAM.logConfig import logConfig
from datetime import datetime
from .colorsFont import colors

def archiveValidation(archive:str) -> bool:
    dictLogging = logConfig()
    for value in dictLogging['archives']:
        if archive == value:
            return archive

    print(colors('red') + f"{archive} not exist in LogConfig.")
    archive = False
    return archive

def messageSizeValidation(message:str) -> str:
    dictLogging = logConfig()
    if dictLogging['length_message'] == 'NO_LIMIT':
        return message
    else:
        return message[0:int(dictLogging['length_message'])-1]


def levelValidation(level:str) -> bool:
    dictLogging = logConfig()
    for value in dictLogging['levels']:
        if level == value:
            return level

    print(colors('red') + f"{level} not exist in LogConfig.")
    level = False
    return level

def dateFormat() -> str:
    configsLogging = logConfig()
    try:
        date_format = configsLogging['date_format']
    except:
        date_format = None
    if date_format == None:
        date = str(datetime.now())
    else:
        now = datetime.now()
        try:
            date = str(now.strftime(date_format))
        except:
            print(colors('red')+f"Date format in LogConfig is invalid.")
            date = False
    return date

def eventValidation(event:str) -> bool:
    dictLogging = logConfig()
    for value in dictLogging['events']:
        if event == value:
            return event

    print(colors('red') + f"{event} not exist in LogConfig.")
    event = False
    return event
