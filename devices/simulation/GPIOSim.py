import json
class GPIOSim:

    BCM = "BCM"
    OUT = "OUT"
    HIGH = "HIGH"
    LOW = "LOW"

    __shared_state = {}
    data = None
    
    #simulated devices
    heating = None
    temp_sensor = None

    
    def __init__(self):
        print("INIT'''''''''''''''''''''''")
        self.__dict__ = self.__shared_state
        if (self.data == None):
            with open("simulation.conf", "r") as conf_file:
                self.data = json.load(conf_file)
                print(self.data)
        self.temp_sensor = devices.simulation.TempSensorSim()

    def setup(self,gpioNumber,mode):
        print(gpioNumber,mode)

    def setmode(self,mode):
        print(mode)
        
    def output(self,gpioNumber,state):
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

    def tick():
        self.temp_sensor.tick()

