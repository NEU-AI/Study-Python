# main.py -- put your code here!
import pyb
adc=pyb.ADC(pyb.Pin('X19'))
while True:
	pyb.delay(1000)
	val=adc.read()
	print(val)
