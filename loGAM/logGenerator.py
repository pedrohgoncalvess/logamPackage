from loGAM.logConfig import logConfig
from .logValidationsFormats import messageSizeValidation,dateFormat,eventValidation,levelValidation,archiveValidation
from .logArchives import createArchives

def writeLog(message:str,
             archive=logConfig()['default_archive'],
             level=logConfig()['default_level'],
             event=logConfig()['default_event']):


    level = level.upper()
    event = event.upper()
    dictConfiggs = logConfig()
    createArchives(dictConfiggs)

    messageLog = messageSizeValidation(message)
    archiveLog = archiveValidation(archive)
    levelLog = levelValidation(level)
    eventLog = eventValidation(event)
    listaLog = [messageLog,archiveLog,levelLog,eventLog]
    for variable in listaLog:
        if variable == False:
            exit()

    logFormat = dictConfiggs['log_format']
    messageFormat = str(logFormat)
    sepLog = dictConfiggs['sep']
    dateLog = dateFormat()


    dictFormat = {'TIME':dateLog,'EVENT':eventLog,'LEVEL':levelLog,'MESSAGE':messageLog}
    for camp in list(dictFormat.keys()):
        messageFormat = messageFormat.replace(camp,dictFormat[camp])
    messageFormat = messageFormat.replace('[','')
    messageFormat = messageFormat.replace(']', '')
    messageFormat = messageFormat.replace("'", '')
    messageFormat = messageFormat.replace(',', ' '+sepLog)

    path = dictConfiggs['path']+'\\Logs\\'+archive+'.txt'

    with open(path,'a') as arquivo:
        arquivo.write(messageFormat+'\n')

