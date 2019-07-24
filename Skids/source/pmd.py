
from machine import Pin

import time

led1 = Pin(22, Pin.OUT)
led2 = Pin(21, Pin.OUT)
led3 = Pin(26, Pin.OUT)
led4 = Pin(17, Pin.OUT)

leds = [led1, led2, led3, led4]

def gpio_write(pin,value):
  pin.value(value)

def led_set(led,value):
  gpio_write(led,value)


def test():
#初始化循环变量
  i = 0
  while True:
    #将所有LED关闭
    for l in leds:
      l.value(1)
    #开启特定的LED
    leds[i].value(0)
    #计算下一个需要开启的LED编号
    i = (i+1)%3
    #延时1秒
    time.sleep(1)

test()


