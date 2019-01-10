class DeviceStateMachineIf:

    states = {0:"UNDIFIENED",10:"INIT",20:"AUTOMATIC",30:"MANUAL",40:"SERVICE"}
    INIT = 10
    AUTOMATIC = 20
    MANUAL = 30
    SERVICE = 40

    actState = 0

    def __init__(self):
        pass

    def init(self):
        if (self.actState == 0):
            self.actState = 10
            return True
        else:
            return False

    def setAutomatic(self):
        if (self.actState == 10 or self.actState == 30 or self.actState == 40):
            self.actState = 20
            return True
        else:
            return False

    def setManual(self):
        if (self.actState == 10 or self.actState == 20 or self.actState == 40):
            self.actState = 30
            return True
        else:
            return False

    def setService(self):
        if (self.actState == 10 or self.actState == 20 or self.actState == 30):
            self.actState = 40
            return True
        else:
            return False
