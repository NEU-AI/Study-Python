Led跑马灯
------------------
引用必要的头文件
 ::

  from machine 
  import Pin
  import machine
  import time

   【设置LED灯的开关】

 ::

  led_en_pin = Pin(2, Pin.OUT)    #设置led灯的总开关
  led0_pin = Pin(14, Pin.OUT)       #设置led灯0号的开关
  led0=machine.PWM(Pin(14), duty=512) #设置led灯0号的亮度
  led1_pin = Pin(32, Pin.OUT)        #设置led灯1号的开关
  led2_pin = Pin(33, Pin.OUT)     #设置led灯2号的开关
  led3_pin = Pin(27, Pin.OUT)    #设置led灯3号的开关
  time.sleep_ms(400)     #程序执行延长 400#单位毫秒

【设置自定义函数 开启led灯 做成跑马灯效果】

 ::

  def test():
	  while True:
 		  led_en(1)   #开启总开关
		  led1_pin(1)     #开启led1号灯
		  time.sleep_ms(400)  #延迟推进400毫秒
 		  led1_pin(0)  #关闭1号灯
		  time.sleep_ms(400)  #延迟推进400毫秒
 		  led2_pin(1)     #开启led2号灯
		  time.sleep_ms(400)    #延迟推进400毫秒
		  led2_pin(0)     #关闭2号灯
		  time.sleep_ms(400)     #延迟推进400毫秒
		  led3_pin(1)     #开启led3号灯
		  time.sleep_ms(400)  #延迟推进400毫秒
		  led3_pin(0)   #关闭led3号灯
		  time.sleep_ms(400)   #延迟推进400毫秒
		  led0_pin(1)  #开启led0号灯
		  time.sleep_ms(800)   #延迟推进800毫秒
		  led0_pin(0)    #关闭led0号灯
  test()    #使用自定义函数test
