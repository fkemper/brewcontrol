from flowcontrol.Timer import Timer
#from flowcontrol.Scheduler import Scheduler
from flowcontrol.Phase import Phase
from flowcontrol.BrewProgram import BrewProgram
from flowcontrol.BrewProgramExecuter import BrewProgramExcecuter
import time
import datetime

#myScheduler = Scheduler()

myBrewProgram = BrewProgram()
#create some phases
phase1 = Phase("Einmaischen",0,0,10,40,False,True)
phase2 = Phase("Eiweissrast",0,25,0,45,False,True)

#add these phase to the program
myBrewProgram.phases.append(phase1)
myBrewProgram.phases.append(phase2)

#create the excecuter instance
myExcecuter = BrewProgramExcecuter()
myExcecuter.setBrewProgram(myBrewProgram)

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







myScheduler.addPhase(phase1)
myScheduler.addPhase(phase2)

print(myScheduler.getTotalTime())

print(myScheduler)





