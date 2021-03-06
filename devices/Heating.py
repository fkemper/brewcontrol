from devices.DeviceStateMachineIf import DeviceStateMachineIf
#try:
#    import RPi.GPIO as GPIO
#except ImportError:
#    import devices.simulation.GPIOSim as GPIO
from devices.IO import IO as GPIO

class Heating(DeviceStateMachineIf):

    __tempSensor__ = None
    __controller__ = None
    __pwmModul__ = None
    __manualState__ = False
    __gpioNumber__ = 0
    __io__ = None
    switchOutput = False
    setTemperature = 0.0
    __conf__ = None
    __negate__ = False

    def __init__(self,pTempSensor=None,pController=None, pPwmModul = None,
                 pGPIONumber=14):
        super().init()
        self.__tempSensor__ = pTempSensor
        self.__controller__ = pController
        self.__pwmModul__ = pPwmModul
        self.__gpioNumber__ = pGPIONumber
        self.gpio = GPIO()
        #config the gpio
        self.gpio.setmode(GPIO.BCM)
        self.gpio.setup(self.__gpioNumber__, GPIO.OUT)
        pass


    def setController(self, pController):
        self.__controller__ = pController

    def setTempSensor(self, pTempSensor):
        self.__tempSensor__ = pTempSensor

    def setAutomatic(self):
        super().setAutomatic()

    def setOff(self):
        super().setOff()
        
    def setManual(self):
        super().setManual()
        if (self.actState == self.MANUAL):
            self.gpio.output(self.__gpioNumber__,GPIO.LOW)
        else:
            print("wrong state. Can't execute setManual. Act state is %s", (self.states[self.actState]))

    def setService(self):
        super().setService()

    def setTargetTemperature(self, pTargetTemperature):
        self.setTemperature = pTargetTemperature
        self.__controller__.SetPoint = self.setTemperature

    def setManualState(self, pState):
        if (self.actState == self.MANUAL):
            self.__manualState__ = pState
            self.__io__.output(self.__gpioNumber__,pState,self.__negate__)
        else:
            print("wrong state. Can't execute setManualState. Act state is %s", (self.states[self.actState]))
    def getActState(self):
        return self.gpio.input(self.__gpioNumber__)
    def tick(self):
        #self.__controller__.SetPoint = self.setTemperature
        #print("ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ")
        if (self.actState == self.AUTOMATIC):
            if (self.__controller__ != None):
                self.__controller__.update(self.__tempSensor__.getTemperature())
                
                #self.__controller__.update(18)
                pwm_setpoint = (self.setTemperature -self.__controller__.output)/self.setTemperature 
                print(str(pwm_setpoint))
                self.__pwmModul__.tick(pwm_setpoint)
                print(str(self.__controller__.output),str(self.__pwmModul__.output))
                self.gpio.output(self.__gpioNumber__, self.__pwmModul__.output)
        if (self.actState == self.OFF):
            print("Zustand ist AAAAUUUUSSSS")
            self.gpio.output(self.__gpioNumber__, False)
        pass

