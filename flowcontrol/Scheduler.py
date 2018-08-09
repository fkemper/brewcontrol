class Scheduler():
    __phases = []
    __actualPhaseIdx = 0

    """Append a phase at end of list"""
    def addPhase(self, phase):
        self.__phases.append(phase)

    """Delete the phase from list"""
    def delPhase(self, index):
        self.__phase.pop(index)

    """Move up the entry in the list"""
    def moveUpPhase(self,index):
        tmpPhase = self.__phase.pop(index)
        self.__phase.insert(index-1)

    """get the total actual still to expired duration of all phases in list"""
    def getTotalTime(self):
        totalDuration = None #in ms
        for phase in self.__phases:
            if (totalDuration != None):
                totalDuration = totalDuration + phase.getDuration()
            else:
                totalDuration = phase.getDuration()
        return totalDuration

    """get the next phase from list"""
    def getNextPhase(self):
        self.__actualPhaseIdx = self.__actualPhaseIdx + 1
        if (self.__actualPhaseIdx > len(self.__phases) -1):
            return None
        else:
            return self.__phases(self.__actualPhaseIdx)

    def __str__(self):
        rep_as_string = ""
        for phase in self.__phases:
            rep_as_string += "Name: " + phase.getName() + " Ziel-Temperatur: " + str(phase.getTargetTemp()) + " °C\n"
        return rep_as_string
