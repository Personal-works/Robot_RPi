import time
import RPi.GPIO as GPIO

def __rotary_init__(self)
	GPIO.setmode(GPIO.BCM)

def rotary_encoder(self,preA,pinA,pinB,):
	if preA==1:
		if preA!=GPIO.input(pinA):
			if GPIO.input(pinB)==1:
				rotarycount += 1
			else:
				rotarycount -= 1
	else:
		if preA!=GPIO.input(pinA):
			if GPIO.input(pinB)==1:
				rotarycount -= 1
			else:
				rotarycount += 1
	preA=GPIO.input(pinA)
	time.sleep(0.005)


if '__name__'=='__main__':
	while 1:
		rotary(27,22)
		countt=1100+rotarycount*50
		print countt
		pwm.setPWM(11,0,countt)


