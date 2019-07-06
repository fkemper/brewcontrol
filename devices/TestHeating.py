from devices.Heating import Heating
from controller.PID import PID
from devices.TempSensor import TempSensor
from controller.PWMModul import PWM
from base.Config import Config
#create all hardware-device-instances
__tempSensor__ = TempSensor()
__pid__ = PID(1, 0, 0)
#self.__pid__.SetPoint = 0.5
__pid__.setSampleTime(0.01)
__pwm__ = PWM(10)
__heating__ = Heating(__tempSensor__,__pid__,__pwm__)
__heating__.setManual()
__heating__.setManualState(True)
