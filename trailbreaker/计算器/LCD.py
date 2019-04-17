


import lcd_show
from lcd_show import *
import pyb
from pyb import Pin

#LCD
usrspi = USR_SPI(scl=Pin('X6',Pin.OUT_PP), sda=Pin('X7', Pin.OUT),dc=Pin('X8', Pin.OUT))
disp = DISPLAY(usrspi,cs=Pin('X5', Pin.OUT),res=Pin('X4', Pin.OUT),led_en=Pin('X3', Pin.OUT))

disp.clr(disp.PINK)
disp.put_vline(8,5,40,disp.RED)
disp.put_vline(15,5,60,disp.GREEN)
disp.put_hline(40,120,50,disp.RED)
disp.put_hline(40,130,80,disp.GREEN)  
a=["1","+","2","=","3"]
disp.putrect(100,100,10,25,0x0ff0)
disp.putstr(6,5,a,0xf0f0)
disp.putstr(6,6," gu yue ",0x0f0f)
disp.putstr_back(6,7," gu yue ",0x0000,0xffff)
disp.putstr_back(6,8," gu yue ",0x0000,0xffff)
disp.put_circle(63,79,50,disp.BLUE)

print(123456)
















