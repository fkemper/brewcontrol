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

import time
import datetime

myDeviceManager = DeviceManager()

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
    myTestHeating.tick()
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





