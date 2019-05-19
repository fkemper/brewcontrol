import time 
from IO import IO

test_io = IO()
test_io.setmode(IO.BCM)
test_io.setup(14,IO.OUT)
test_io.output(14,False)
i = 0
print(str(test_io.getTemperature()))
while i<5:
    test_io.tick()
    time.sleep(1)
    i = i + 1
    print(str(test_io.getTemperature())) 
test_io.output(14,True)
i = 0
while i<5:
    test_io.tick()
    time.sleep(1)
    i = i + 1
    print(str(test_io.getTemperature())) 
