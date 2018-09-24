class ControllerStateMachineIf:

    STATES = {"UNDIFIENED":0,"INIT":10,"OFF":20,"AUTOMODE":30,"MANUALMODE":40}
    actState = 0

    def __init__(self):
        pass

    def init(self):
        if (self.actState == STATES["UNDIFIENED"]):
            self.actState = STATES["INIT"]
            return True
        else:
            return False

    def autommode(self):
        if (self.actState == STATES["OFF"] or self.actState == STATES["MANUALMODE"]):
            self.actState = STATES["AUTOMODE"]
            return True
        else:
            return False
            
    def manualmmode(self):
        if (self.actState == STATES["OFF"] or self.actState == STATES["AUTOMODE"]):
            self.actState = STATES["MANUALMODE"]
            return True
        else:
            return False

    def off(self):
        if (self.actState == STATES["INIT"] or self.actState == STATES["AUTOMODE"] or self.actState == STATES["MANUALMODE"]):
            self.actState = STATES["OFF"]
            return True
        else:
            return False
