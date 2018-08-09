from flowcontrol.BrewProgramStateMachineIf import BrewProgramStateMachineIf
from flowcontrol.Timer import Timer
import time

class BrewProgramExcecuter(BrewProgramStateMachineIf):

    __brewProgram__ : None
    __timer__ : None

    def __init__(self):
        pass

    def setBrewProgram(self, brewProgram):
        self.__brewProgram__ = brewProgram

    def startBrewProgram(self):
        if super().start():
            self.__timer__.start()
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
                self.__timer__ = Timer(self.__brewProgram__.phases[0].getDuration())
                self.__timer__.init()
            # initialisere den Timer mit den Zeitwerten der 1. Phase aus dem Programm
            print("to do implemt")
        else:
            print("wrong state. Can't execute init. Act state is %s", (self.states[self.actState]))

    def __nextPhase(self):
        self.__timer__ = Timer(self.__brewProgram__.phases[1].getDuration())
        self.__timer__.init()
        self.__timer__.start()

    def stoppBrewProgram(self):
        if super().init():
            # beende / breche die Ausführung des Programms ab. Gebe die verschiedneen Resourcen frei und stoppe diverse
            # Prozesse
            print("to do implemt")
        else:
            print("wrong state. Can't execute stopp. Act state is %s", (self.states[self.actState]))

    """zyklische Funktion die in Abhängigkeit von dem aktuellen Zustand des Brauprogramms"""
    def tick(self):
        self.__timer__.tick()
        if (self.actState == self.STARTED):
            if (self.__timer__.isElapsed()):
                print("next Pjhase")
                self.__nextPhase()
        if (self.actState == self.PAUSED):
            print("Programm pausiert")

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



