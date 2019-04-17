
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
            print(data)
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

Number=[
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

temp= Number
result=[0,0,0,0,0,0,0,0]
for i in range(8):
	for j in range(8):
		temp[i][j]=temp[i][j]<<i
	print(temp[i])
for i in range(8):
	for j in  range(8):
		result[i]=result[i]+temp[j][i]
'''
def show_4_number(number):
	temp=Number
	result=[0,0,0,0,0,0,0,0]
	number=list(number)
	for p in range(4):
			for j in range(8):
				temp[int(number[p])][j]=temp[i][j]<<p
'''
def disp_test():
	spi = USR_SPI(scl=Pin('X1',Pin.OUT_PP), sda=Pin('X3',Pin.OUT_PP))
	display = AIP1638(spi,cs=Pin('X2',Pin.OUT_PP))
	print("AIP1638 control interface init done")

	display.disp_on()
	display._data(b"\x40")#设为开始输入数据
	s=(b"\xC0")
	for  i in  range(8):
		s+=pack('<H', result[i])
	print(result)
	print(s)
	display._data(s)
	
	while True:
		print("AIP1638 disp")
		pyb.delay(1000)
		display.disp_on()
		pyb.delay(1000)
		display.disp_off()
		
disp_test()