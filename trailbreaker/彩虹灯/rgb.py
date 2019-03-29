from pyb import Pin,Timer
rgb=[Pin(i, Pin.OUT_PP) for i in ['Y1','Y2','Y3']]#初始化引脚
tm3=Timer(3,freq=100)#初始化时钟
tm8=Timer(8,freq=100)
tm4=Timer(4,freq=100)
intensity_red=0#初始化亮度
intensity_gre=33
intensity_blu=66
red=tm3.channel(1,Timer.PWM,pin=Pin.cpu.C6)#启用时钟3的1通道，设置为pwm模式
gre=tm8.channel(2,Timer.PWM,pin=Pin.cpu.C7)
blu=tm4.channel(3,Timer.PWM,pin=Pin.cpu.B8)
while True:#rgb变色
	while intensity_red<99:
		red.pulse_width_percent(intensity_red)
		intensity_red=(intensity_red+1)%100
		pyb.delay(10)
	while intensity_gre<99:
		gre.pulse_width_percent(intensity_gre)
		intensity_gre=(intensity_gre+1)%100
		pyb.delay(10)
	while intensity_blu<99:
		blu.pulse_width_percent(intensity_blu)
		intensity_blu=(intensity_blu+1)%100
		pyb.delay(10)
	while intensity_red>0:
		red.pulse_width_percent(intensity_red)
		intensity_red=(intensity_red-1)%100
		pyb.delay(10)
	while intensity_gre>0:
		gre.pulse_width_percent(intensity_gre)
		intensity_gre=(intensity_gre-1)%100
		pyb.delay(10)
	while intensity_blu>0:
		blu.pulse_width_percent(intensity_blu)
		intensity_blu=(intensity_blu-1)%100
		pyb.delay(10)
