import pyb
leds = [pyb.LED(i) for i in range(1,5)]
sw=pyb.Switch()
j=0
def test():
	global j
	j=j+1	
sw.callback(test)
for l in leds:
	l.off()
n = 0
try:
	while True:
		if j%2==0:
			n = (n + 1) % 4
			leds[n].toggle()
			pyb.delay(50)
		else :
			n = (n + 1) % 4
			leds[3-n].toggle()
			pyb.delay(50)
finally:
	for l in leds:
		l.off()
