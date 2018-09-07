from flowcontrol.PID import PID



if __name__ == "__main__":
	
	pid = PID(0.5, 1, 0.001)

	pid.SetPoint=0.5
	pid.setSampleTime(0.01)
	
	while(True):
		pid.update(0.0)
		print(str(pid.output) + "\n")
		
		
	

