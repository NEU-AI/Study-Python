让LED灯亮起来
------------------
【引用必要的头文件】
 ::

  from machine import Pin
  import machine
【设置LED灯】
 ::

  led_en_pin = Pin(2, Pin.OUT)    #设置总开关
  led0_pin = Pin(14, Pin.OUT)  #设置单个灯的开关
  led0=machine.PWM(Pin(14), duty=512) 

【开启开关】
 ::

  led_en(1)

