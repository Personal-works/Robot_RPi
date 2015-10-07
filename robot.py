from Adafruit_PWM_Servo_Driver import PWM
import time

pwm=PWM(0x40)

pwm.setPWMFreq(60)
print 'set Freq 60'
dicts={11:'280-410,open->close',10:'220-540, left-right',9:'220-540,low-high',8:'180-600(350mid),high-low',7:'385,mid',6:'220-470,right-left' }
setd=[]

while(True):
	print 'loop'
	for ii in range(0,7,+1):
		print 'forloop'
		print dicts.get(ii)
		setd.append(input('input the degree...'))
	for tt in range(11,5,-1):
		pwm.setPWM(tt,0,setd[11-tt])

	



