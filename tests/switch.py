from machine import Switch
import utime

pins = [36,39,34,35]
keys = []

for i in range(4):
  keys.append(Switch(i))

while True:
  result = ""
  for k in keys:
    if k():
      result += "Press"
    else:
      result += "Up\t"
    result += "\t"
  print(result)
  utime.sleep_ms(200)
  


