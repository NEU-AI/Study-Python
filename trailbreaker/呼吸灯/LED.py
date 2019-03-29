from pyb import Pin,Timer
tm2=Timer(2,freq=100)#初始化时钟
tm3=Timer(3,freq=100)
intensity4=0#初始化亮度
intensity3=0
led4=tm3.channel(1,Timer.PWM,pin=Pin.cpu.B4)#启用时钟3的1通道，设置为pwm模式
led3=tm2.channel(1,Timer.PWM,pin=Pin.cpu.A15)
while True:
	while intensity3<99:#逐渐变亮
		led3.pulse_width_percent(intensity3)
		intensity3=(intensity3+1)%100
		pyb.delay(50)
	while intensity4<99:
		led4.pulse_width_percent(intensity4)
		intensity4=(intensity4+1)%100
		pyb.delay(50)
	while intensity3>0:#达到最亮时逐渐变暗
		led3.pulse_width_percent(intensity3)
		intensity3=(intensity3-1)%100
		pyb.delay(50)
	while intensity4>0:
		led4.pulse_width_percent(intensity4)
		intensity4=(intensity4-1)%100
		pyb.delay(50)
	
