import pyb
leds = [pyb.LED(i) for i in range(1,5)]#定义LED灯
sw=pyb.Switch()#定义按键
j=0
def test():
	global j
	j=j+1	
sw.callback(test)#按下按键时调用test函数
for l in leds:#初始化：将所有灯熄灭
	l.off()
n = 0
try:
	while True:
		if j%2==0:#j是偶数正向亮
			n = (n + 1) % 4
			leds[n].toggle()
			pyb.delay(50)
		else :#j是奇数反向亮
			n = (n + 1) % 4
			leds[3-n].toggle()
			pyb.delay(50)
finally:
	for l in leds:
		l.off()
