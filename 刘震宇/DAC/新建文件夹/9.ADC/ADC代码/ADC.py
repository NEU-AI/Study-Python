# main.py -- put your code here!
import pyb
from pyb import Pin
import time
from struct import pack
class USR_SPI:
    def __init__(self,scl,sda):
        self.scl = scl
        self.sda = sda
    def write_data(self,buf):
        for data in buf:
            #print(data)
            pyb.delay(1)
            for i in range (8): #send data
                self.scl(0)
                if data & (0x01):
                    self.sda(1)
                else:
                    self.sda(0)
                self.scl(1)
                data = data >> 1

class AIP1638:
    def __init__(self, spi, cs):
        self.spi = spi
        self.cs = cs

    def _data(self, data):
        self.cs(0)
        pyb.delay(1)
        self.spi.write_data(data)
        pyb.delay(1)
        self.cs(1)

    def disp_on(self):
        self._data(b"\x8d")

    def disp_off(self):
        self._data(b"\x80")

Number=[#0
[1,1,1,1, 1 , 1 , 0 ,0 ],
	#1
	[ 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 ],
	#2
	[ 01 , 01 , 00 , 01 , 01 , 00 , 01 , 00 ],
	#3
	[ 01 , 01 , 01 , 01 , 00 , 00 , 01 , 00 ],
	#4
	[ 00 , 01 , 01 , 00 , 00 , 01 , 01 , 00 ],
	#5
	[ 01 , 00 , 01 , 01 , 00 , 01 , 01 , 00 ],
	#6
	[ 01 , 00 , 01 , 01 , 01 , 01 , 01 , 00 ],
	#7
	[ 01 , 01 , 01 , 00 , 00 , 00 , 00 , 00 ],
	#8
	[ 01 , 01 , 01 , 01 , 01 , 01 , 01 , 00 ],
	#9
	[ 01 , 01 , 01 , 01 , 00 , 01 , 01 , 00 ]
]


result=[0,0,0,0,0,0,0,0]
def show_4_number(num):
	global result
	num=list(num)
	result=[0,0,0,0,0,0,0,0]
	temp =Number
	code1=[[0 for col in range(8)] for row in range(10)]
	if len(num)>1:
		code2=[[0 for col in range(8)] for row in range(10)]
	if len(num)>2:
		code3=[[0 for col in range(8)] for row in range(10)]
	if len(num)>3:
		code4=[[0 for col in range(8)] for row in range(10)]

	for j in range(8):
		code1[int(num[0])][j]=temp[int(num[0])][j]<<0
		if len(num)>1:
			code2[int(num[1])][j]=temp[int(num[1])][j]<<1
		if len(num)>2:
			code3[int(num[2])][j]=temp[int(num[2])][j]<<2
		if len(num)>3:
			code4[int(num[3])][j]=temp[int(num[3])][j]<<3
	for i in range(8):
		result[i]=result[i]+code1[int(num[0])][i]
		if len(num)>1:
			result[i]=result[i]+code2[int(num[1])][i]
		if len(num)>2:
			result[i]=result[i]+code3[int(num[2])][i]
		if len(num)>3:
			result[i]=result[i]+code4[int(num[3])][i]

	print(result)
adc=pyb.ADC(pyb.Pin('Y11'))
while True:
	spi = USR_SPI(scl=Pin('X1',Pin.OUT_PP), sda=Pin('X3',Pin.OUT_PP))
	display = AIP1638(spi,cs=Pin('X2',Pin.OUT_PP))
	pyb.delay(1000)
	val=adc.read()
	show_4_number(str(val))
	display.disp_on()
	display._data(b"\x40")#设为开始输入数据
	s=(b"\xC0")
	for  i in  range(8):
		s+=pack('<H', result[i])
	display._data(s)
	print(val)
