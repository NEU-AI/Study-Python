


import lcd_show
from lcd_show import *
from font import *
import pyb
from pyb import Pin
import time
import utime
from random import randint
import framebuf
#LCD
usrspi = USR_SPI(scl=Pin('X6',Pin.OUT_PP), sda=Pin('X7', Pin.OUT),dc=Pin('X8', Pin.OUT))
disp = DISPLAY(usrspi,cs=Pin('X5', Pin.OUT),res=Pin('X4', Pin.OUT),led_en=Pin('X3', Pin.OUT))
disp.clr(disp.PINK)
def flag_Germany():
    disp.putrect(20,20,100,20,disp.BLACK)
    disp.putrect(20,40,100,20,disp.RED)
    disp.putrect(20,60,100,20,disp.ORANGE)


def flag_French():
    disp.putrect(20,20,20,90,disp.BLUE)
    disp.putrect(40,20,20,90,disp.WHITE)
    disp.putrect(60,20,20,90,disp.RED)

def flag_Japan():
    disp.putrect(20,20,90,60,WHITE)
    disp.put_circle_back(65,50,20,disp.WHITE)

flag_Germany()
#flag_French()
#flag_Japan() 




	

















