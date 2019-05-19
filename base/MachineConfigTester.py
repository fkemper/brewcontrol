from MashineConfig import MachineConfig 

conf = MachineConfig()
print(conf.conf.items())
testdict = conf.conf.items()
for item in testdict:
    print(item[0])
    item[1] = { 23:"Fritz"}
print(conf.conf.items())

