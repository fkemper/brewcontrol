from devices.DeviceStateMachineIf import DeviceStateMachineIf

class TempSensor(DeviceStateMachineIf):

    __manualState__ = False

    def __init__(self):
        pass

    def setAutomatic(self):
        super().setAutomatic()

    def setManual(self):
        super().setManual()

    def setService(self):
        super().setService()

    def tick(self):
        #read the act value from the hardware input
        pass
