import datetime
from io import StringIO
from flowcontrol.TimerStateMachineIf import TimerStateMachineIf


class Timer(TimerStateMachineIf):

    __duration = None
    __elapsedTime = None
    __oldTimeStamp = None

    def __init__(self,duration):
        self.__duration = duration
        print(self.__duration)

    """init the timer"""
    def init(self):
        if (super().init()):
            self.__elapsedTime = datetime.timedelta(hours=0,minutes=0,seconds=0)
            pass
        else:
            print("wrong state. Can't execute init. Act state is %s", (self.states[self.actState]))

    """start the timer"""
    def start(self):
        if (super().start()):
            pass
        else:
            print("wrong state. Can't execute start. Act state is %s", (self.states[self.actState]))

    """stopp the timer (and reset)"""
    def stopp(self):
        if (super().stopp()):
            elapsedTime = datetime.timedelta(0)
        else:
            print("wrong state. Can't execute stopp. Act state is %s", (self.states[self.actState]))

    """pause the timer"""
    def pause(self):
        if (super().pause()):
            pass
        else:
            print("wrong state. Can't execute pause. Act state is %s", (self.states[self.actState]))

    """return the True if the actual state is ELAPSED"""
    def isElapsed(self):
        return self.actState == self.ELAPSED

    """return the True if the actual state is PAUSED"""
    def isPaused(self):
        return self.actState == self.PAUSED

    """return the actual elapsed time"""
    def getElapsedTime(self):
        return self.__elapsedTime

    """return the end-time"""
    def getEndTime(self):
        return datetime.datetime.now() + self.__duration - self.__elapsedTime


    """update all time-values depends on act state of timer"""
    def tick(self):
        if (self.actState == self.STARTED):
            actTimeStamp = datetime.datetime.now()
            if (self.__oldTimeStamp != None):
                self.__elapsedTime += actTimeStamp - self.__oldTimeStamp
            if (self.__elapsedTime > self.__duration):
                self.elapsed()
        self.__oldTimeStamp = datetime.datetime.now()

    """return a string representation of this timer"""
    def __str__(self):
        return "einggestellte Zeit: %s\nabgelaufene Zeit: %s\nendet um: %s\naktuelle Zeit: %s\naktueller Zustand: %s" % (str(self.__duration), (str(self.__elapsedTime)).split(".")[0], str(self.getEndTime().time()).split(".")[0], datetime.datetime.now().strftime("%H:%M:%S"), self.states[self.actState])
