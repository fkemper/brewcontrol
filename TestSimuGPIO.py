from devices.simulation.GPIOSim import GPIOSim

sim = GPIOSim()
sim.setmode(3)
sim.output(3,GPIOSim.HIGH)

sim.output(4,GPIOSim.HIGH)
sim.output(3,GPIOSim.LOW) 

