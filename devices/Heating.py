from devices.DeviceStateMachineIf import DeviceStateMachineIf

class Heating(DeviceStateMachineIf):

    __tempSensor__ = None
    __controller__ = None
    __manualState__ = False

    switchOutput = False
    setTemperature = 0.0

    def __init__(self,pTempSensor=None,pController=None):
        self.__tempSensor__ = pTempSensor
        self.__controller__ = pController
        pass


    def setController(self, pController):
        self.__controller__ = pController

    def setTempSensor(self, pTempSensor):
        self.__tempSensor__ = pTempSensor

    def setAutomatic(self):
        super().setAutomatic()

    def setManual(self):
        super().setManual()

    def setService(self):
        super().setService()

    def setManualState(self, pState):
        if (self.actState == self.MANUAL):
            self.__manualState__ = pState
        else:
            print("wrong state. Can't execute setManualState. Act state is %s", (self.states[self.actState]))

    def tick(self):
        if (self.__controller__ != None):
            self.__controller__.update(0.4)
            print(str(self.__controller__.output))
        pass

