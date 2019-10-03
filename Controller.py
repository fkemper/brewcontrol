from flowcontrol.BrewProgram import BrewProgram
from flowcontrol.BrewProgramExecuter import BrewProgramExcecuter
from devices.DeviceManager import DeviceManager
from flowcontrol.Phase import Phase
import time

class controller():
    def __init__(self):

        self.myBrewProgram = BrewProgram()
        self.myBrewProgram.name = "Test-Program"
        # create some phases
        phase1 = Phase("Einmaischen", 0, 0, 5, 25, False, True)
        phase2 = Phase("Eiweissrast", 0, 0, 5, 45, False, True)
        phase3 = Phase("MALTROSERAST", 0, 0, 3, 20, False, True)

        # add these phase to the program
        self.myBrewProgram.phases.append(phase1)
        self.myBrewProgram.phases.append(phase2)
        self.myBrewProgram.phases.append(phase3)
        self.devManager = DeviceManager()

        self.prgExcecuter = BrewProgramExcecuter()
        self.prgExcecuter.setBrewProgram(self.myBrewProgram)
        self.prgExcecuter.setDeviceManager(self.devManager)

    def startBrewProgram(self):
        print("starte Brauprogramm")
        self.prgExcecuter.startBrewProgram()
    def initBrewProgram(self):
        self.prgExcecuter.setBrewProgram(self.myBrewProgram)
        self.prgExcecuter.initBrewProgram()
    def stopBrewProgram(self):
        self.prgExcecuter.stoppBrewProgram()
    def pauseBrewProgram(self):
        print("pausiere Brauprogramm")
        self.prgExcecuter.pauseBrewProgram()
    def getBrewProgram(self):
        print("Brauprogramm wurde abgefragt")
        return self.myBrewProgram

    def getActUiValues(self):
        uiValues = {}
        footerViewValues = {}
        monitoringViewValues = {}
        brewprogrammViewValues = {}
        
        if (self.prgExcecuter.actState == BrewProgramExcecuter.STARTED):
            footerViewValues.update(actTemp=self.devManager.getTempSensor().getTemperature())
            footerViewValues.update(self.prgExcecuter.getActPhaseDatas())
            footerViewValues.update(self.prgExcecuter.getActProgrammDatas())
            monitoringViewValues.update(dict(actStateHeating=self.devManager.getHeating().getActState()))
            #actStateDisher=self.devManager.getDisher().getActState())
            brewprogrammViewValues.update(dict(actPhaseId=self.prgExcecuter.getActPhaseDatas()['phaseId']))
            uiValues.update(dict(footerViewValues=footerViewValues,monitoringViewValues=monitoringViewValues,brewprogrammViewValues=brewprogrammViewValues))
        else:
            uiValues.update(dict(actTemp='---'))

        print(uiValues)
        return uiValues
        #return 111.11

    def getActBrewProgramState(self):
        return self.prgExcecuter.actState

    def start(self):
        print("Controller-loop gestartet")
        self.prgExcecuter.initBrewProgram()
        while True:
            self.prgExcecuter.tick()
            self.devManager.tick()
            time.sleep(0.1)
    def initUi(self):
        uiValues = {}
        uiValues.update(dict(programName="Test-Bier",totalTime=self.prgExcecuter.getTotalTime()))

        return uiValues
