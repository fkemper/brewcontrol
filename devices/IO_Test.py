import time 
from IO import IO

test_io = IO()
test_io.output(3,"HIGH")
print(str(test_io.getTemperature()))
while 1:
    test_io.tick()
    time.sleep(1)

    print(str(test_io.getTemperature())) 
