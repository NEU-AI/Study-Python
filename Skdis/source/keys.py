from machine import Pin
import utime
#1B
#pins = [36,39,34,35]
#1C
pins = [36,39,34,35]
keys = []

for p in pins:
  keys.append(Pin(p,Pin.IN))

while True:
  result = ""
  for k in keys:
    if k.value():
      result += "Up\t"
    else:
      result += "Press\t"
    result += "\t"
  print(result)
  utime.sleep_ms(1000)
