
# main.py -- put your code here!

import pyb
from pyb import Pin

adc = pyb.ADC(pyb.Pin('X4'))
led =Pin('X3', Pin.OUT_PP)

#adc = pyb.ADC(pyb.Pin.cpu.A0)    # create an ADC on pin X19
val = adc.read()

# y = a*x + b
# y1 = 25, x1 =10
# y2 = 50, x2 = 3.603
# a = (y2-y1)/(x2-x1)
# b = y1 - x1*a
#  |  \
#  |   * (50,3.603k)
#  |    \
#  |     \
#  |      * (25,10k)
#  |       \
#  |---------------

a = (50-25)/(3.603-10)
b = 25 - 10*a

def readTemp():
  val = adc.read()
  vin = val*3.3/4095  #管脚电压值
  vtemp = vin/2.5     #头电压值 
                                 #                +------------> vtemp
  rtemp = (vtemp*14.7)/(3.3-vtemp) # 3.3-----[14.7K R5]--|--[rtemp]-----gnd 探头电阻值
  ctemp = a*rtemp + b  #温度
  
  if ctemp > 38 :
	led.value(1);
  else :
	led.value(0);
	
  print("val=",val, "vin=",vin)
  print("vtemp=",vtemp,"rtemp=",rtemp)
  print("ctemp=",ctemp)
  
while 1:
  readTemp()
  pyb.delay(1000)

