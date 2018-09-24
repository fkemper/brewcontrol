from controller.PID import PID
from controller.ControllerStateMachine import ControllerStateMachineIf

class Controller(ControllerStateMachineIf):

	__pid_controller = PID(1,1,1)
	P = 0.0
	I = 0.0
	D = 0.0
	
	
	def init(self):
		if super.init():
			self.off()
			pass
		else:
			print("wrong state. Can't execute init. Act state is %s", (self.STATES.getKey[self.actState]))
			
	def setAutomode(self):
		if super.automode():
			#todo
			pass
		else:
			print("wrong state. Can't execute setAutomode. Act state is %s", (self.STATES.getKey[self.actState]))
			
	def setManualmode(self):
		if super.manualmode():
			#todo
			pass
		else:
			print("wrong state. Can't execute setmanualmode. Act state is %s", (self.STATES.getKey[self.actState]))
			

			

	
