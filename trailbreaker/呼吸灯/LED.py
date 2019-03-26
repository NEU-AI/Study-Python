from pyb import Pin,Timer
tm2=Timer(2,freq=100)
tm3=Timer(3,freq=100)
intensity4=0
intensity3=0
led4=tm3.channel(1,Timer.PWM,pin=Pin.cpu.B4)
led3=tm2.channel(1,Timer.PWM,pin=Pin.cpu.A15)
while True:
	while intensity3<99:
		led3.pulse_width_percent(intensity3)
		intensity3=(intensity3+1)%100
		pyb.delay(50)
	while intensity4<99:
		led4.pulse_width_percent(intensity4)
		intensity4=(intensity4+1)%100
		pyb.delay(50)
	while intensity3>0:
		led3.pulse_width_percent(intensity3)
		intensity3=(intensity3-1)%100
		pyb.delay(50)
	while intensity4>0:
		led4.pulse_width_percent(intensity4)
		intensity4=(intensity4-1)%100
		pyb.delay(50)
	
