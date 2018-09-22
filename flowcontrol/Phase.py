import datetime

class Phase():
    __name = ""
    __time = 0
    __temp = 0
    __timeElapsed = False
    __elapseMode = False
    __duration = None
    __notification = False

    def __init__(self,name,hours,minutes,seconds,target_temperature,mode,notification):
        self.__name = name
        self.__duration = datetime.timedelta(hours=hours,minutes=minutes,seconds=seconds)
        self.__temp = target_temperature
        self.__notification = notification

    def getDuration(self):
        return self.__duration

    def getName(self):
        return self.__name

    def getTargetTemp(self):
        return self.__temp

    def getNotificationFlag(self):
        return self.__notification

    def __str__(self):
        return "Hi"

