from devices.Heating import Heating
from controller.PID import PID
from devices.TempSensor import TempSensor
from controller.PWMModul import PWM


class DeviceManager():
    __heating__ = None
    __tempSensor__ = None
    __pid__ = None
    __pwm__ = None

    def __init__(self):
        #create all hardware-device-instances
        self.__tempSensor__ = TempSensor()
        self.__pid__ = PID(1, 0, 0)
        #self.__pid__.SetPoint = 0.5
        self.__pid__.setSampleTime(0.01)
        self.__pwm__ = PWM(10)
        self.__heating__ = Heating(self.__tempSensor__,self.__pid__,self.__pwm__)
        pass

    def tick(self):
        self.__tempSensor__.tick()
        self.__heating__.tick()


    def getHeating(self):
        return self.__heating__

    def getTempSensor(self):
        return self.__tempSensor__
