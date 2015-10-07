import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(02,GPIO.OUT)
GPIO.setup(03,GPIO.IN)

GPIO.output(02,0)
time.sleep(1)


while 1:
	GPIO.output(02,1)
	time.sleep(0.00001)
	GPIO.output(02,0)

	while GPIO.input(03)==0:
		start=time.time()
	#	print start
	while GPIO.input(03)==1:
		stop=time.time()
	#	print stop
	distance=(stop-start)*34000
	distance=distance/2
	
	print "d is : %.1f" %distance
	time.sleep(0.5)




