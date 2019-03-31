from devices.DeviceStateMachineIf import DeviceStateMachineIf
try:
    import RPi.GPIO as GPIO
except ImportError:
    import devices.simulation.GPIOSim as GPIO

class Heating(DeviceStateMachineIf):

    __tempSensor__ = None
    __controller__ = None
    __pwmModul__ = None
    __manualState__ = False
    __gpioNumber__ = 0

    switchOutput = False
    setTemperature = 0.0

    def __init__(self,pTempSensor=None,pController=None, pPwmModul = None, pGPIONumber=0):
        self.__tempSensor__ = pTempSensor
        self.__controller__ = pController
        self.__pwmModul__ = pPwmModul
        self.__gpioNumber__ = pGPIONumber

        #config the gpio
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__gpioNumber__, GPIO.OUT)
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

    def setTargetTemperature(self, pTargetTemperature):
        self.setTemperature = pTargetTemperature
        self.__controller__.SetPoint = self.setTemperature

    def setManualState(self, pState):
        if (self.actState == self.MANUAL):
            self.__manualState__ = pState
        else:
            print("wrong state. Can't execute setManualState. Act state is %s", (self.states[self.actState]))

    def tick(self):
        if (self.__controller__ != None):
            self.__controller__.update(self.__tempSensor__.getTemperature())
            self.__pwmModul__.tick(0.5)
            print(str(self.__controller__.output),str(self.__pwmModul__.output))
            GPIO.output(self.__gpioNumber__, GPIO.HIGH)
        pass
