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

if (__name__ == "__main__"):
    myDeviceManager = DeviceManager()
    myTempSensorSim = TempSensor()
    cycTime = cycleTime()

    duration = 0

    timedelta = 0
    while (duration < 20):

        myTempSensorSim.tick(cycTime.getTimeDelta())
        time.sleep(1)
        duration = duration + 1




    myBrewProgram = BrewProgram()
    # create some phases
    phase1 = Phase("Einmaischen", 0, 0, 10, 40, False, True)
    phase2 = Phase("Eiweissrast", 0, 0, 5, 45, False, True)
    phase3 = Phase("MALTROSERAST", 0, 0, 3, 20, False, True)

    # add these phase to the program
    myBrewProgram.phases.append(phase1)
    myBrewProgram.phases.append(phase2)
    myBrewProgram.phases.append(phase3)

    duration = 0
    while (duration > 500):
        myTempSensorSim.tick(cycTime.getTimeDelta())
        myDeviceManager.tick()
        time.sleep(0.05)
        duration += 1




    #myBrewController = BrewController()
    #myRestServer = RestServer()
    #myRestServer.setBrewController(myBrewController)
    #myRestServer.start_server()


    #create the excecuter instance
    myExcecuter = BrewProgramExcecuter()
    myExcecuter.setBrewProgram(myBrewProgram)
    myExcecuter.setDeviceManager(myDeviceManager)

    print(myExcecuter.getTotalTime())
    myExcecuter.startBrewProgram()
    myExcecuter.initBrewProgram()
    myExcecuter.startBrewProgram()

    duration = 0
    while (duration < 300):
        myTempSensorSim.tick(cycTime.getTimeDelta())
        myDeviceManager.tick()
        myExcecuter.tick()

        time.sleep(0.05)
        duration += 1

    myExcecuter.pauseBrewProgram()
    duration = 0
    while (duration < 7):
        myDeviceManager.tick()
        myExcecuter.tick()
        time.sleep(1)
        duration += 1
    myExcecuter.startBrewProgram()
    duration = 0
    while (duration < 5):
        myDeviceManager.tick()
        myExcecuter.tick()
        time.sleep(1)
        duration += 1







#myScheduler.addPhase(phase1)
#myScheduler.addPhase(phase2)

#print(myScheduler.getTotalTime())

#print(myScheduler)





