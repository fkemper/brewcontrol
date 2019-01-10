from devices.Heating import Heating
from controller.PID import PID
from devices.TempSensor import TempSensor


class DeviceManager():
    __heating__ = None
    __tempSensor__ = None
    __pid__ = None

    def __init__(self):
        #create all hardware-device-instances
        self.__tempSensor__ = TempSensor()
        self.__pid__ = PID(1, 1, 0.001)
        self.__pid__.SetPoint = 0.5
        self.__pid__.setSampleTime(0.01)
        self.__heating__ = Heating(self.__tempSensor__,self.__pid__)
        pass

    def tick(self):
        self.__heating__.tick()
        self.__tempSensor__.tick()

    def getHeating(self):
        return self.__heating__