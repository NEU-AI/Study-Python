二氧化碳传感器
------------------
模块介绍
^^^^^^^^^^^^^^^^^^^^^
此实验使用MH-Z14A二氧化碳模块

*实物图：

MH-Z14A二氧化碳模块

.. image:: ../picture/co2.jpg
   :width: 300px
   :height: 200px

接线
^^^^^^^^^
二氧化碳模块T连接TB板X2（UART4_RX),
二氧化碳模块R连接TB板X1（UART4_TX),
二氧化碳模块V+连接TB板3V3,
二氧化碳模块V-连接TB板GND

编程学习
^^^^^^^^^
打开main.py文件开始编写代码:

导入头文件:

 :: 

	import pyb
	import time
	import json
	from pyb import Pin
	from pyb import UART
	class MHZ14A():
		PACKET = [0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]#读气体浓度值命令
		ZERO = [0xff, 0x01, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0x78]#校准传感器零点命令
		def __init__(self):#初始化
			self.uart = UART(4, 9600,bits=8,parity = None)                        
			time.sleep(2)
		def zero(self):#校准零点
			#print(bytearray(MHZ14A.ZERO))
			self.uart.write(bytearray(MHZ14A.ZERO))
		
		def get(self):#读取气体浓度
			self.uart.write(bytearray(MHZ14A.PACKET))
			#print(bytearray(MHZ14A.PACKET))
			res=self.uart.read(9)
			#print(res)
			#print(len(res))
			#for i in range(0,len(res))
			res = bytearray(res)
			checksum = 0xff & (~(res[1] + res[2] + res[3] + res[4] + res[5] + res[6] + res[7]) + 1)
			if res[8] == checksum:#校验
				print('ppm:',((res[2] << 8) | res[3]))
				#print(res[4])
				return {
					"ppm": (res[2] << 8) | res[3]
				}
			else:
				print ("checksum: " + hex(checksum))
				return -1
		def deinit(self):
			self.uart.deinit()


	if __name__ == '__main__':
		A=MHZ14A()
		A.zero()
		A.get()
		A.deinit()
		while(1):
			A=MHZ14A()
			#A.zero()
			A.get()
			A.deinit()




实验现象
^^^^^^^^^^^^^^^^^^^^^

加载程序。显示空气中二氧化碳浓度。

.. image:: ../picture/ppm.png
   :width: 300px
   :height: 400px
