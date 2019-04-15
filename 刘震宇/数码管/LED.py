
import pyb
from pyb import Pin
import time
from led8seg import *


spi = USR_SPI(scl=Pin('X1',Pin.OUT_PP), sda=Pin('X3',Pin.OUT_PP))
display = AIP1638(spi,cs=Pin('X2',Pin.OUT_PP))
print("AIP1638 control interface init done")

display.disp_on()
display._data(b"\x40")
display._data(b"\xC0\xf0\x00\x0f\x00\x0f\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00")

while True:
print("AIP1638 disp")
pyb.delay(1000)
display.disp_on()
pyb.delay(1000)
display.disp_off()

disp_test()







