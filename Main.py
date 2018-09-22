from flowcontrol.Timer import Timer
#from flowcontrol.Scheduler import Scheduler
from flowcontrol.Phase import Phase
from flowcontrol.BrewProgram import BrewProgram
from flowcontrol.BrewProgramExecuter import BrewProgramExcecuter
from flowcontrol.BrewController import BrewController
from restconnector.RestServer import RestServer

import time
import datetime

myBrewController = BrewController()
myRestServer = RestServer()
myRestServer.setBrewController(myBrewController)
myRestServer.start_server()


#create the excecuter instance
myExcecuter = BrewProgramExcecuter()
#myExcecuter.setBrewProgram(myBrewProgram)

print(myExcecuter.getTotalTime())
myExcecuter.startBrewProgram()
myExcecuter.initBrewProgram()
myExcecuter.startBrewProgram()

duration = 0
while (duration < 5):
    myExcecuter.tick()
    time.sleep(1)
    duration += 1
myExcecuter.pauseBrewProgram()
duration = 0
while (duration < 5):
    myExcecuter.tick()
    time.sleep(1)
    duration += 1
myExcecuter.startBrewProgram()
duration = 0
while (duration < 5):
    myExcecuter.tick()
    time.sleep(1)
    duration += 1







#myScheduler.addPhase(phase1)
#myScheduler.addPhase(phase2)

#print(myScheduler.getTotalTime())

#print(myScheduler)





