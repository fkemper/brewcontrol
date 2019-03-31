from flowcontrol.BrewProgramStateMachineIf import BrewProgramStateMachineIf 
from flowcontrol.Timer import Timer
import time

class BrewProgramExcecuter(BrewProgramStateMachineIf):

    __brewProgram__ =  None
    __timer__ = None
    __actPhase__ = None
    __actPhaseId__ = 0

    def __init__(self):
        pass

    def setBrewProgram(self, brewProgram):
        self.__brewProgram__ = brewProgram

    def setDeviceManager(self, pDeviecManager):
        self.__deviceManager = pDeviecManager

    def startBrewProgram(self):
        if super().start():
            self.__actPhase__ =self.__brewProgram__.phases[self.__actPhaseId__]
            self.__deviceManager.getHeating().setTargetTemperature(self.__actPhase__.getTargetTemp())
            #self.__timer__.start()
        else:
            print("wrong state. Can't execute start. Act state is %s", (self.states[self.actState]))

    def pauseBrewProgram(self):
        if super().pause():
            self.__timer__.pause()
        else:
            print("wrong state. Can't execute pause. Act state is %s", (self.states[self.actState]))

    def initBrewProgram(self):
        if super().init():
            if (self.__brewProgram__ != None):
                self.__actPhaseId__ = 0
                self.__timer__ = Timer(self.__brewProgram__.phases[self.__actPhaseId__].getDuration())
                print("setze Temp auf wert ", self.__brewProgram__.phases[self.__actPhaseId__].getTargetTemp())
                self.__timer__.init()
            # initialisere den Timer mit den Zeitwerten der 1. Phase aus dem Programm
            print("to do implemt")
        else:
            print("wrong state. Can't execute init. Act state is %s", (self.states[self.actState]))

    def __nextPhase(self):
        self.__actPhaseId__ = self.__actPhaseId__ +1
        self.__timer__ = Timer(self.__brewProgram__.phases[self.__actPhaseId__].getDuration())
        self.__timer__.init()

        self.__deviceManager.getHeating().setTargetTemperature(self.__brewProgram__.phases[self.__actPhaseId__].getTargetTemp())
        print("setze Temp auf wert ", self.__brewProgram__.phases[self.__actPhaseId__].getTargetTemp())
        #self.__timer__.start()

    def stoppBrewProgram(self):
        if super().init():
            # beende / breche die Ausfuehrung des Programms ab. Gebe die verschiedneen Resourcen frei und stoppe diverse
            # Prozesse
            print("to do implemt")
        else:
            print("wrong state. Can't execute stopp. Act state is %s", (self.states[self.actState]))

    """zyklische Funktion die in Abhaengigkeit von dem aktuellen Zustand des Brauprogramms"""
    def tick(self):
        if (self.actState == self.STARTED):
            if (self.__deviceManager.getTempSensor().getTemperature() >=
                self.__brewProgram__.phases[self.__actPhaseId__].getTargetTemp() and
                self.__timer__.actState != Timer.STARTED):
                self.__timer__.start()
                
            if (self.__timer__.isElapsed()):
                print("next Phase")
                self.__nextPhase()
        if (self.actState == self.PAUSED):
            print("Programm pausiert")
        self.__timer__.tick()

        print(self.__timer__)

    """get the total actual still to expired duration of all phases in list"""
    def getTotalTime(self):
        totalDuration = None  # in ms
        for phase in self.__brewProgram__.phases:
            if (totalDuration != None):
                totalDuration = totalDuration + phase.getDuration()
            else:
                totalDuration = phase.getDuration()
        return totalDuration


    def getActPhaseDatas(self):
        datas = {}
        datas.update(dict(phaseId=self.__actPhaseId__,phaseName=self.__brewProgram__.phases[self.__actPhaseId__].getName(),duration=self.__brewProgram__.phases[self.__actPhaseId__].getDuration(),targetTemp=self.__brewProgram__.phases[self.__actPhaseId__].getTargetTemp(),elapsedTime=self.__timer__.getElapsedTime()))
        return datas
