import ubitmap
import screen
import time
import text
import network
from machine import UART,Pin
import utime
from umqtt.simple import MQTTClient
screen.clear()

class pics():
	def __init__(self):
		self.keys = [Pin(p, Pin.IN) for p in [35, 36, 39, 34]]
		self.keymatch = ["Key1", "Key2", "Key3", "Key4"]
		self.select=1
		self.displayInit()
		self.wifi_name = "NEUI"
		self.wifi_SSID = "NEUI3187"
		#MQTT服务端信息
		self.SERVER = "112.125.89.85"   #MQTT服务器地址
		self.SERVER_PORT = 3881         #MQTT服务器端口
		self.DEVICE_ID = "wc001"        #设备ID
		self.TOPIC1 = b"/cloud-skids/online/dev/" + self.DEVICE_ID
		self.TOPIC2 = b"/cloud-skids/message/server/" + self.DEVICE_ID
		self.CLIENT_ID = "f25410646a8348f8a1726a3890ad8f73"
		self.uart = UART(1, baudrate=115200, bits=8, parity=0, rx=18, tx=19, stop=1)
		#设备状态
		self.ON = "1"
		self.OFF = "0"
		self.d=" "
		self.c = MQTTClient(self.CLIENT_ID, self.SERVER, self.SERVER_PORT)
	def drawInterface(self):
		bmp1=ubitmap.BitmapFromFile("pic/boy")
		bmp2=ubitmap.BitmapFromFile("pic/girl")
		bmp1.draw(20,200)
		bmp2.draw(140,200)
		screen.drawline(0, 160, 240, 160, 2, 0xff0000)
		
	def do_connect(self):
		sta_if = network.WLAN(network.STA_IF)    #STA模式
		ap_if = network.WLAN(network.AP_IF)      #AP模式
		if ap_if.active():
			ap_if.active(False)                  #关闭AP
		if not sta_if.isconnected():
			print('Connecting to network...')
		sta_if.active(True)                      #激活STA
		sta_if.connect(self.wifi_name, self.wifi_SSID)     #WiFi的SSID和密码
		while not sta_if.isconnected():
			pass
		print('Network config:', sta_if.ifconfig())
		gc.collect()
	def selectInit(self):
		screen.drawline(20, 200, 92, 200, 2, 0xff0000)
		screen.drawline(92, 200, 92, 272, 2, 0xff0000)
		screen.drawline(92, 272, 20, 272, 2, 0xff0000)
		screen.drawline(20, 272, 20, 200, 2, 0xff0000)
	def displayInit(self):
		screen.clear()
		self.drawInterface()
		self.selectInit()
	def esp(self):
		self.c.set_callback(self.sub_cb)    #设置回调
		self.c.connect()
		print("连接到服务器：%s" % self.SERVER)
		self.c.publish(self.TOPIC1, self.ON)     #发布“1”到TOPIC1
		self.c.subscribe(self.TOPIC2)       #订阅TOPIC
		#display.text("从微信取得信息", 20, 20, 0xf000, 0xffff)
	
	
	
	
	def keyboardEvent(self, key):
        # 右移选择键
		if self.keymatch[key] == "Key1":
			if self.select%2==1:
				screen.drawline(20, 200, 92, 200, 2, 0xffffff)
				screen.drawline(92, 200, 92, 272, 2, 0xffffff)
				screen.drawline(92, 272, 20, 272, 2, 0xffffff)
				screen.drawline(20, 272, 20, 200, 2, 0xffffff)
				screen.drawline(140, 200, 212, 200, 2, 0xff0000)
				screen.drawline(212, 200, 212, 272, 2, 0xff0000)
				screen.drawline(212, 272, 140, 272, 2, 0xff0000)
				screen.drawline(140, 272, 140, 200, 2, 0xff0000)
				self.select+=1
			else:
				screen.drawline(140, 200, 212, 200, 2, 0xffffff)
				screen.drawline(212, 200, 212, 272, 2, 0xffffff)
				screen.drawline(212, 272, 140, 272, 2, 0xffffff)
				screen.drawline(140, 272, 140, 200, 2, 0xffffff)
				screen.drawline(20, 200, 92, 200, 2, 0xff0000)
				screen.drawline(92, 200, 92, 272, 2, 0xff0000)
				screen.drawline(92, 272, 20, 272, 2, 0xff0000)
				screen.drawline(20, 272, 20, 200, 2, 0xff0000)
				self.select+=1
		if self.keymatch[key] == "Key3":
			if self.select%2==1:
				bmp1=ubitmap.BitmapFromFile("pic/boy")
				bmp1.draw(140,40)
				self.d="001"
				self.c.publish(self.TOPIC2,self.d)
			else:
				bmp2=ubitmap.BitmapFromFile("pic/girl")
				bmp2.draw(140,40)
				self.d="002"
				self.c.publish(self.TOPIC2,self.d)
	def sub_cb(self,topic, message):
		message = message.decode()
		print("服务器发来信息：%s" % message)
		#global count
		if message=="001":
			bmp1=ubitmap.BitmapFromFile("pic/boy")
			bmp1.draw(140,40)
		elif message=="002":
			bmp1=ubitmap.BitmapFromFile("pic/girl")
			bmp1.draw(140,40)
		
					
				
	def start(self):
		try:
			while True:
				self.c.check_msg()
				i = 0
				j = -1
				for k in self.keys:
					if (k.value() == 0):
						if i != j:
							j = i
							self.keyboardEvent(i)
					i = i + 1
					if (i > 3):
						i = 0
				time.sleep_ms(130)
		finally:
				self.c.disconnect()
				print("MQTT连接断开")
			
if __name__ == '__main__':
	p = pics()
	p.do_connect()
	p.esp()
	p.start()
			
			
			
			
			
			