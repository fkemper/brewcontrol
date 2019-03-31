import sys
import json
import os
import os.path
from base.Config import Config
from devices.simulation.TempSensorSim import TempSensor
try:
    import RPi.GPIO as GPIO
except ImportError:
    pass

class IO:

    BCM = "BCM"
    BOARD = "BOARD"
    OUT = "OUT"
    HIGH = "HIGH"
    LOW = "LOW"

    __shared_state = {}
    data = None
    confHolder = None
    simulation =  None

    #simulated devices
    heating = None
    temp_sensor = None

    def __init__(self):
        self.__dict__ = self.__shared_state
        print("INIT'''''''''''''''''''''''")
        self.confHolder = Config()
        self.simulation = self.confHolder.conf["simulation"]["simulation_activ"]
        print( self.simulation)
        if (self.data == None):
            with open("simulation.conf", "r") as conf_file:
                self.data = json.load(conf_file)
                print(self.data)
        self.temp_sensor = TempSensor()

    def setup(self,gpioNumber,mode):
        if (not self.simulation):
            if(mode==self.BCM):
                mode = GPIO.BCM
            elif(mode==self.BOARD):
                mode = GPIO.BOARD
            GPIO.setup(gpioNumber,mode)
    def setmode(self,mode):
        if (not self.simulation):
            GPIO.setmode(gpioNumber,mode)
    def output(self,gpioNumber,state):
        if (not self.simulation):
            GPIO.output(gpioNumber,state)
        else:
            event = self.data[str(gpioNumber)]["order"]
            if (event == "SWITCH_HEATING_ON_OFF"):
                if (state == "HIGH"):
                    print("Heizung einschalten")
                else:
                    print("Heizung ausschalten")
            if (event == "SWITCH_DISHER_ON_OFF"):
                if (state == "HIGH"):
                    print("Ruehrwerk einschalten")
                else:
                    print("Ruehrwerk ausschalten")
            print()
            print(gpioNumber,state)

    def getTemperature(self):

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
            return rueckgabewert
    def tick(self):

        self.temp_sensor.tick(100)
