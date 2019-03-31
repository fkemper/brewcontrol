from base.Config import Config
import os.path

class TempSensor():

    __manualState__ = False
    __temperature__ = 0
    confHolder = None
    _x_ = 0

    def __init__(self):
        self.confHolder = Config()
        pass

    def tick(self,pTimeDelta):
        if (os.path.exists(self.confHolder.conf["simulation"]["temperature_sensor_file_name"])):
            file = open(self.confHolder.conf["simulation"]["temperature_sensor_file_name"],"w")

            self._x_ = self._x_ + pTimeDelta * 0.25
            file.write("33 00 4b 46 ff ff 02 10 f4 : crc=f4 YES\n33 00 4b 46 ff ff 02 10 f4 t=%05d" % (self._x_))
            file.close()
            print("##################### %05d" % self._x_)
    pass
