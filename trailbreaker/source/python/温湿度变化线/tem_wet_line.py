import pyb
from pyb import UART
from pyb import Pin
import time
import lcd_show
import font
from lcd_show import *
from font import *
import utime
from random import randint
import framebuf
usrspi = USR_SPI(scl=Pin('X6',Pin.OUT_PP), sda=Pin('X7', Pin.OUT),dc=Pin('X8', Pin.OUT))
disp = DISPLAY(usrspi,cs=Pin('X5', Pin.OUT),res=Pin('X4', Pin.OUT),led_en=Pin('X3', Pin.OUT))
x1=40
y=0
x2=80
disp.clr(disp.WHITE)
class DHT11:
    def __init__(self,pin_):
        #self.data=[]
        self.PinName=pin_
        time.sleep(1)
        self.N1 = Pin(pin_, Pin.OUT_PP)
        #start work
        #N2.low()
        pyb.delay(10)
    def read_temps(self):
        data=[]
        j=0
        N1 = Pin(self.PinName, Pin.OUT_PP)
        #N1=self.N1
        N1.low()
        time.sleep_ms(20)
        N1.high()
		time.sleep_us(30)
        #wait to response
        N1 = Pin(self.PinName,Pin.IN)
        while N1.value()==1:
		#print('1')
		continue
        while N1.value()==0:
		#print('2')
		continue
        while N1.value()==1:
		#print('3')
		continue
        #get data
        while j<40:
            k=0
            while N1.value()==0:
                continue
            while N1.value()==1:
		#print(k)
                k+=1
                if k>100:break
            if k<3:
                data.append(0)
            else:
                data.append(1)
            j=j+1
        print('Sensor is working')
	#print(k)
        j=0
        #get temperature
        humidity_bit=data[0:7]
        humidity_point_bit=data[8:15]
        temperature_bit=data[16:23]
        temperature_point_bit=data[24:31]
        check_bit=data[32:39]
        humidity=0
        humidity_point=0
        temperature=0
        temperature_point=0
        check=0
        for i in range(7):
            humidity+=humidity_bit[i]*2**(7-i)
            humidity_point+=humidity_point_bit[i]*2**(7-i)
            temperature+=temperature_bit[i]*2**(7-i)
            temperature_point+=temperature_point_bit[i]*2**(7-i)
            check+=check_bit[i]*2**(7-i)
        tmp=humidity+humidity_point+temperature+temperature_point
        if check==tmp:
            print('temperature is',temperature,'wet is',humidity,'%')
	    global x1,y,x2
	    disp.putpixel(x1+(temperature-25)*3,y,disp.RED)
	    disp.putpixel(x2+(humidity-15)*3,y,disp.BLUE)
	    y+=1
        else:
            print('SHUJUCUOWU',humidity,humidity_point,temperature,temperature_point,check)
        return str(temperature)+','+str(humidity)
while 1:
	S=DHT11('Y4')
	A=S.read_temps()
	#print(A)
	pyb.delay(100)

