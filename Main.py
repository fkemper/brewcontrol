from flowcontrol.Timer import Timer
#from flowcontrol.Scheduler import Scheduler
from flowcontrol.Phase import Phase
from flowcontrol.BrewProgram import BrewProgram
from flowcontrol.BrewProgramExecuter import BrewProgramExcecuter
from flowcontrol.BrewController import BrewController
from restconnector.RestServer import RestServer
from devices.Heating import Heating
from controller.PID import PID
from devices.DeviceManager import DeviceManager
from devices.simulation.TempSensorSim import  TempSensor
from base.Config import Config
from ui.gtk3.MainWIndow import MainWindow
import threading
import json
import datetime

import time
import datetime

class cycleTime():

    oldtimestamp = datetime.datetime.now()
    def getTimeDelta(self):
        now = datetime.datetime.now()
        timedelta = (now - self.oldtimestamp) / datetime.timedelta(milliseconds=1)

        self.oldtimestamp = now
        return timedelta
class controller():
    def __init__(self):

        self.myBrewProgram = BrewProgram()
        # create some phases
        phase1 = Phase("Einmaischen", 0, 0, 30, 40, False, True)
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
        self.prgExcecuter.initBrewProgram()
        self.prgExcecuter.startBrewProgram()

    def pauseBrewProgram(self):
        print("pausiere Brauprogramm")
        self.prgExcecuter.pauseBrewProgram()
    def getBrewProgram(self):
        print("Brauprogramm wurde abgefragt")

    def getActUiValues(self):
        uiValues = {}
        if self.prgExcecuter.actState == BrewProgramExcecuter.STARTED:
            uiValues.update(dict(actTemp=self.devManager.getTempSensor().getTemperature()))
            uiValues.update(self.prgExcecuter.getActPhaseDatas())
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

if (__name__ == "__main__"):
    #read the config-file and make it accesable "like" a singleton
    with open("brewcontrol.conf", "r") as conf_file:
        data = json.load(conf_file)
    confHolder = Config()
    confHolder.conf = data

    cycTime = cycleTime()
    ctr = controller()
    #start gtk3 gui
    if (confHolder.conf["interface"]["gtk3"]["enable"]):
        myUi = MainWindow()
        myUi.set_controller(ctr)
        myUi.initialize_ui(ctr.myBrewProgram)
        myThread = threading.Thread(target=myUi.start)
        myThread.start()

    #start webserver
    if (confHolder.conf["interface"]["web_interface"]["enable"]):
        webInterface = RestServer()
        webInterface.start_server()


    myDeviceManager = DeviceManager()
    myTempSensorSim = TempSensor()

    duration = 0

    timedelta = 0
    while (duration < 2):

        myTempSensorSim.tick(cycTime.getTimeDelta())
        time.sleep(1)
        duration = duration + 1

    threading.Thread(target=ctr.start).start()
    while True:
        pass



    duration = 0
    while (duration > 500):
        myTempSensorSim.tick(cycTime.getTimeDelta())
        myDeviceManager.tick()
        time.sleep(0.05)
        duration += 1








