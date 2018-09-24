import datetime

class PWM():

    __timebase__ = 0.5
    __lowerPoint__ = 0.0
    __heigherPoint__ = 1.0
    __diff__ = 0.0
    __timestamp__ = datetime.datetime(2000,1,1,0,0,0,0)

    output = False


    def __init__(self):
        pass

    def tick(self,input):
        diff = (datetime.datetime.utcnow() - self.__timestamp__).total_seconds()
        if (diff > self.__timebase__):
            self.__timestamp__ = datetime.datetime.utcnow()
        else:
            self.output = (diff >= (self.__timebase__ * input))


