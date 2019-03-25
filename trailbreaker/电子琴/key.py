from pyb import Pin,Timer
'''
R1=Pin('X9',Pin.OUT_PP)
R2=Pin('X10',Pin.OUT_PP)
R3=Pin('Y3',Pin.OUT_PP)
R4=Pin('Y4',Pin.OUT_PP)
C1=Pin(‘Y5’,Pin.IN,Pin.PULL_UP)
C2=Pin(‘Y6’,Pin.IN,Pin.PULL_UP)
C3=Pin(‘Y7’,Pin.IN,Pin.PULL_UP)
C4=Pin(‘Y8’,Pin.IN,Pin.PULL_UP)
'''
x1 = Pin('X3',Pin.OUT_PP)
R=[Pin('X9',Pin.OUT_PP),Pin('X10',Pin.OUT_PP),Pin('Y3',Pin.OUT_PP),Pin('Y4',Pin.OUT_PP)]
C=[Pin(‘Y5’,Pin.IN,Pin.PULL_UP),Pin(‘Y6’,Pin.IN,Pin.PULL_UP),Pin(‘Y7’,Pin.IN,Pin.PULL_UP),Pin(‘Y8’,Pin.IN,Pin.PULL_UP)]
i=0
j=0
while True:
	for i in range(0,4):
		R[i].low()
		for j in range(0,4):
			if i==0&&j==0&&C[j].value()==0
				tm3=Timer(2, freq=262)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==0&&j==1&&C[j].value()==0
				tm3=Timer(2, freq=294)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==0&&j==2&&C[j].value()==0
				tm3=Timer(2, freq=330)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==0&&j==3&&C[j].value()==0
				tm3=Timer(2, freq=349)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==1&&j==0&&C[j].value()==0
				tm3=Timer(2, freq=392)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==1&&j==1&&C[j].value()==0
				tm3=Timer(2, freq=440)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==1&&j==2&&C[j].value()==0
				tm3=Timer(2, freq=494)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==1&&j==3&&C[j].value()==0
				tm3=Timer(2, freq=523)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==2&&j==0&&C[j].value()==0
				tm3=Timer(2, freq=587)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==2&&j==1&&C[j].value()==0
				tm3=Timer(2, freq=659)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==2&&j==2&&C[j].value()==0
				tm3=Timer(2, freq=698)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==2&&j==3&&C[j].value()==0
				tm3=Timer(2, freq=784)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==3&&j==0&&C[j].value()==0
				tm3=Timer(2, freq=880)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==3&&j==1&&C[j].value()==0
				tm3=Timer(2, freq=988)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==3&&j==2&&C[j].value()==0
				tm3=Timer(2, freq=1047)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
			elif i==3&&j==3&&C[j].value()==0
				tm3=Timer(2, freq=1175)
				buzzer=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
				
