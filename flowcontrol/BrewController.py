from flowcontrol.Timer import Timer
#from flowcontrol.Scheduler import Scheduler
from flowcontrol.Phase import Phase
from flowcontrol.BrewProgram import BrewProgram
from flowcontrol.BrewProgramExecuter import BrewProgramExcecuter
import json


class BrewController():

    def __init__(self):
        self.myBrewProgram = BrewProgram()
        # create some phases
        phase1 = Phase("Einmaischen", 0, 0, 10, 40, False, True)
        phase2 = Phase("Eiweissrast", 0, 25, 0, 45, False, True)
        phase3 = Phase("MALTROSERAST", 0, 30, 0, 20, False, True)

        # add these phase to the program
        self.myBrewProgram.phases.append(phase1)
        self.myBrewProgram.phases.append(phase2)
        self.myBrewProgram.phases.append(phase3)

    def get_actual_phases_list(self):
        return self.myBrewProgram.phases
