
import pyb
from pyb import Pin
import time

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

def disp_test():
    spi = USR_SPI(scl=Pin('X1',Pin.OUT_PP), sda=Pin('X3',Pin.OUT_PP))
    display = AIP1638(spi,cs=Pin('X2',Pin.OUT_PP))
    print("AIP1638 control interface init done")

    display.disp_on()
    display._data(b"\x40")#设为开始输入数据
    display._data(b"\xC0\xf0\x00\x0f\x00\x0f\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00")
	#设置初始地址为00
    while True:
        print("AIP1638 disp")
        pyb.delay(1000)
        display.disp_on()
        pyb.delay(1000)
        display.disp_off()
        
disp_test()







