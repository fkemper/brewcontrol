import time 
from IO import IO

test_io = IO()
test_io.setmode(IO.BCM)
test_io.setup(17,IO.OUT)
test_io.output(17,False)

print(str(test_io.getTemperature()))
while 1:
    test_io.tick()
    time.sleep(1)

    print(str(test_io.getTemperature())) 
