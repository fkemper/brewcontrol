from devices.DeviceStateMachineIf import DeviceStateMachineIf
from base.Config import Config
import os.path
class TempSensor(DeviceStateMachineIf):

    __manualState__ = False
    __temperature__ = 0
    confHolder = None

    def __init__(self):
        self.confHolder = Config()
        pass

    def setAutomatic(self):
        super().setAutomatic()

    def setManual(self):
        super().setManual()

    def setService(self):
        super().setService()

    def tick(self):
        #read the act value from the hardware input
        # 1-wire Slave Datei lesen
        if (self.confHolder.conf["simulation"]["simulation_activ"]):
            print("vvvvvvvvvvvvvvvvvvvvv",self.confHolder.conf["simulation"]["simulation_activ"])
            if (os.path.exists(self.confHolder.conf["simulation"]["temperature_sensor_file_name"])): 
                file = open(self.confHolder.conf["simulation"]["temperature_sensor_file_name"])
        else:
            if (os.path.exist('/sys/bus/w1/devices/28-000005d2e508/w1_slave')):
                file = open('/sys/bus/w1/devices/28-000005d2e508/w1_slave')
        if (file != None):
            filecontent = file.read()
            file.close()

            # Temperaturwerte auslesen und konvertieren
            stringvalue = filecontent.split("\n")[1].split(" ")[9]
            temperature = float(stringvalue[2:]) / 1000

            # Temperatur ausgeben
            rueckgabewert = '%6.2f' % temperature
            self.__temperature__ = rueckgabewert
            print("############################" + str(rueckgabewert))

    def getTemperature(self):
        return float(self.__temperature__)
    pass
