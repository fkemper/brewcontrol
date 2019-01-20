
class TempSensor():

    __manualState__ = False
    __temperature__ = 0
    _x_ = 0

    def __init__(self):
        pass

    def tick(self,pTimeDelta):

        file = open('E:/1_slave','w')
        self._x_ = self._x_ + pTimeDelta * 0.25
        file.write("33 00 4b 46 ff ff 02 10 f4 : crc=f4 YES\n33 00 4b 46 ff ff 02 10 f4 t=%05d" % (self._x_))
        file.close()
        print("##################### %05d" % self._x_)
    pass
