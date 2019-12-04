from pyb import Pin
import pyb

leds = [Pin(i, Pin.OUT_PP) for i in ['X9','Y6','Y7','Y8']]
#Pin.cpu.B6,Pin.cpu.B13,Pin.cpu.B14,Pin.cpu.B15
print(leds[0])
print(leds[1])
print(leds[2])
print(leds[3])
leds[0].value(0)
pyb.delay(1000)
leds[0].value(1)
pyb.delay(2000)
leds[0].value(0)

leds[1].value(0)
pyb.delay(1000)
leds[1].value(1)
pyb.delay(2000)
leds[1].value(0)

leds[2].value(0)
pyb.delay(1000)
leds[2].value(1)
pyb.delay(2000)
leds[2].value(0)

leds[3].value(0)
pyb.delay(1000)
leds[3].value(1)
pyb.delay(2000)
leds[3].value(0)
