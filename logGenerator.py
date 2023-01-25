from logConfig import logConfig,loadConfig
from logValidationsFormats import messageSizeValidation,dateFormat,eventValidation,levelValidation

def writeLog(message:str,
             archive=logConfig()['default_archive'],
             level=logConfig()['default_level'],
             event=logConfig()['default_event']):
    dictConfiggs = logConfig()
    sepLog = dictConfiggs['sep']
    logFormat = dictConfiggs['log_format']
    messageLog = messageSizeValidation(message)
    dateLog = dateFormat()
    archiveLog = archive
    levelLog = levelValidation()
    messageFormat = str(logFormat)
    eventLog = eventValidation(event)

    dictFormat = {'time':dateLog,'event':}
    for camp in logFormat:
        messageFormat.replace(camp)


    print(sepLog,logFormat,messageLog,dateLog,archiveLog,levelLog)

writeLog('PEDRO HENRIQUE GONCALVES CARLOS PEDRO HENRIQUE GONCALVES CARLOS PEDRO HENRIQUE GONCALVES CARLOS')
print(logConfig())
