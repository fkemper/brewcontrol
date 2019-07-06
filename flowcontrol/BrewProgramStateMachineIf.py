class BrewProgramStateMachineIf:

    states = {0:"UNDIFIENED",10:"INIT",20:"STARTED",30:"STOPPED",40:"PAUSED",50:"ENDED"}
    INIT = 10
    STARTED = 20
    STOPPED = 30
    PAUSED = 40
    ELAPSED = 50
    actState = 0

    def __init__(self):
        pass

    def init(self):
        if (self.actState == 0 or self.actState == 30):
            self.actState = 10
            return True
        else:
            return False

    def start(self):
        if (self.actState == 10 or self.actState == 30 or self.actState == 40):
            self.actState = 20
            return True
        else:
            return False

    def stopp(self):
        if (self.actState == 20 or self.actState == 40):
            self.actState = 30
            return True
        else:
            return False

    def pause(self):
        if (self.actState == 20):
            self.actState = 40
            return True
        else:
            return False

    def elapsed(self):
        if (self.actState == 20):
            self.actState = 50
            return True
        else:
            return False
