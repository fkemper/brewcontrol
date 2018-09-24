from controller.PWMModul import PWM
import time

if __name__ == "__main__":
    myPWM = PWM()
    while 1:
        myPWM.tick(0.2)
        print("Ausgang : "+ str(myPWM.output))


