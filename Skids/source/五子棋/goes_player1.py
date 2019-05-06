import ubitmap
import screen
import time
import text
import network
from machine import UART,Pin
import utime
from umqtt import MQTTClient
import framebuf

class GOES():
	def __init__(self):
		self.screen_width = 200
		self.screen_height = 280
		self.keys = [Pin(p, Pin.IN) for p in [35, 36, 39, 34]]
		self.keymatch = ["Key1", "Key2", "Key3", "Key4"]
		self.board=[
					[[20,20,0],[40,20,0],[60,20,0],[80,20,0],[100,20,0],[120,20,0],[140,20,0],[160,20,0],[180,20,0],[200,20,0],[220,20,0]],
					[[20,40,0],[40,40,0],[60,40,0],[80,40,0],[100,40,0],[120,40,0],[140,40,0],[160,40,0],[180,40,0],[200,40,0],[220,40,0]],
					[[20,60,0],[40,60,0],[60,60,0],[80,60,0],[100,60,0],[120,60,0],[140,60,0],[160,60,0],[180,60,0],[200,60,0],[220,60,0]],
					[[20,80,0],[40,80,0],[60,80,0],[80,80,0],[100,80,0],[120,80,0],[140,80,0],[160,80,0],[180,80,0],[200,80,0],[220,80,0]],
					[[20,100,0],[40,100,0],[60,100,0],[80,100,0],[100,100,0],[120,100,0],[140,100,0],[160,100,0],[180,100,0],[200,100,0],[220,100,0]],
					[[20,120,0],[40,120,0],[60,120,0],[80,120,0],[100,120,0],[120,120,0],[140,120,0],[160,120,0],[180,120,0],[200,120,0],[220,120,0]],
					[[20,140,0],[40,140,0],[60,140,0],[80,140,0],[100,140,0],[120,140,0],[140,140,0],[160,140,0],[180,140,0],[200,140,0],[220,140,0]],
					[[20,160,0],[40,160,0],[60,160,0],[80,160,0],[100,160,0],[120,160,0],[140,160,0],[160,160,0],[180,160,0],[200,160,0],[220,160,0]],
					[[20,180,0],[40,180,0],[60,180,0],[80,180,0],[100,180,0],[120,180,0],[140,180,0],[160,180,0],[180,180,0],[200,180,0],[220,180,0]],
					[[20,200,0],[40,200,0],[60,200,0],[80,200,0],[100,200,0],[120,200,0],[140,200,0],[160,200,0],[180,200,0],[200,200,0],[220,200,0]],
					[[20,220,0],[40,220,0],[60,220,0],[80,220,0],[100,220,0],[120,220,0],[140,220,0],[160,220,0],[180,220,0],[200,220,0],[220,220,0]]
					]#初始化棋子坐标（x坐标，y坐标，颜色）
		self.startX = 20
		self.startY = 20
		self.selectXi = 5
		self.selectYi = 5
		self.displayInit()
		self.color=0x000000#player1棋子颜色为黑色
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

	
	def drawcross(self, x, y, lineColor):# 画选择位置的框
		screen.drawline(x - 10, y-10, x - 5, y-10, 3, lineColor)
		screen.drawline(x - 10, y-10, x - 10, y-5, 3, lineColor)
		screen.drawline(x + 10, y-10, x + 5, y-10, 3, lineColor)
		screen.drawline(x + 10, y-10, x + 10, y-5, 3, lineColor)
		screen.drawline(x - 10, y+10, x - 5, y+10, 3, lineColor)
		screen.drawline(x - 10, y+10, x - 10, y+5, 3, lineColor)
		screen.drawline(x + 10, y+10, x + 5, y+10, 3, lineColor)
		screen.drawline(x + 10, y+10, x + 10, y+5, 3, lineColor)
        		
	
	#画棋盘网格	
	def grid(self):
		x=20
		y=20
		for i in range(11):
			screen.drawline(x, 20, x, 220, 3, 0x000000)
			x+=20
		for j in range(11):
			screen.drawline(20, y, 220, y, 3, 0x000000)
			y+=20
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
		
	def esp(self):
		self.c.set_callback(self.sub_cb)    #设置回调
		self.c.connect()
		print("连接到服务器：%s" % self.SERVER)
		self.c.publish(self.TOPIC1, self.ON)     #发布“1”到TOPIC1
		self.c.subscribe(self.TOPIC2)       #订阅TOPIC
		#display.text("从微信取得信息", 20, 20, 0xf000, 0xffff)
		
	def sub_cb(self,topic, message):#从服务器接受信息
		message = message.decode()
		
		print("服务器发来信息：%s" % message)
		#global count
		t=int(message)#根据接收到的信息解析棋子位置
		j=t//11
		i=t%11
		x = self.board[j][i][0]
		y = self.board[j][i][1]
		if self.board[j][i][2]==0:
			self.put_circle_back(x,y,10,0x00ff00)#在解析出的位置上画绿色棋子
			self.board[j][i][2]=1#将棋子标记为绿色
		self.is_win(i,j,self.board[j][i][2])#判断胜负
	def put_circle_back(self,x,y,r,color):#画圆形棋子
		a=0#选定原点距离圆心距离
		b=r#在原点所画交叉线长度
		di=3-(r<<1)#辅助判断画圆是否结束
		while (a<=b):#选定原点画交叉线
			screen.drawline(x - b, y-a, x + b, y-a, 3, color)
			screen.drawline(x - a, y, x - a, y+b, 3, color)
			screen.drawline(x - b, y-a, x, y-a, 3, color)
			screen.drawline(x - a, y-b, x - a, y, 3, color)
			screen.drawline(x, y+a, x + b, y+a, 3, color)
			screen.drawline(x + a, y-b, x + a, y, 3, color)
			screen.drawline(x + a, y, x + a, y+b, 3, color)
			screen.drawline(x - b, y+a, x, y+a, 3, color)
			a+=1#改变原点位置
			if(di<0):#辅助判断画圆是否结束，计算下一步所画交叉线长度
				di+=4*a+6
			else:
				di+=10+4*(a-b)
				b-=1
			screen.drawline(x + a, y, x + a, y+b, 3, color)
	def selectInit(self):#选择初始化
        # 变量初始化
		self.selectXi = 5
		self.selectYi = 5
		x = self.board[self.selectYi][self.selectXi][0]
		y = self.board[self.selectYi][self.selectXi][1]
        # 选择初始化
		self.drawcross(x, y, 0xff0000)
	# 界面初始化
	def displayInit(self):#开始游戏初始化
		screen.clear()
		self.grid()
		for self.selectYi in range(11):
			for self.selectXi in range(11):
				self.board[self.selectYi][self.selectXi][2]=0
		self.selectInit()
	def is_win(self,i,j,k):#判断胜负

		start_y=0
		end_y=10
		if j-4>=0:
			start_y=j-4
		if j+4<=10:
			end_y=j+4
		count=0
		for pos_y in range(start_y,end_y+1):#判断纵向胜负
			if self.board[pos_y][i][2]==k and k==1:
				count+=1

				if count>=5:
					text.draw("绿色方胜",88,160,0xff0000)
			else:
				count=0
		for pos_y in range(start_y,end_y+1):
			if self.board[pos_y][i][2]==k and k==2:
				count+=1

				if count>=5:
					text.draw("黑色方胜",88,160,0xff0000)
			else:
				count=0
				
		start_x=0
		end_x=10
		if i-4>=0:
			start_x=i-4
		if i+4<=10:
			end_x=i+4
		count=0
		for pos_x in range(start_x,end_x+1):#判断横向胜负
			if self.board[j][pos_x][2]==k and k==1:
				count+=1

				if count>=5:
					text.draw("绿色方胜",88,160,0xff0000)
			else:
				count=0
		for pos_x in range(start_x,end_x+1):
			if self.board[j][pos_x][2]==k and k==2:
				count+=1

				if count>=5:
					text.draw("黑色方胜",88,160,0xff0000)
			else:
				count=0
		
		count=0
		s=j-i
		start=start_y
		end=end_x+s
		if j>i:
			start=start_x+s
			end=end_y
		for index in range(start,end+1):#判断斜方向胜负（左上右下）
			if self.board[index][index-s][2]==k and k==1:
				count+=1

				if count>=5:
					text.draw("绿色方胜",88,160,0xff0000)
			else:
				count=0
		for index in range(start,end+1):
			if self.board[index][index-s][2]==k and k==2:
				count+=1

				if count>=5:
					text.draw("黑色方胜",88,160,0xff0000)
			else:
				count=0
		
		count=0
		s=j+i

		if j+i<=10:
			start=start_y
			end=s-start_x
		if j+i>10:
			start=s-10
			end=10
		if s>=4 and s<=16:

			for index in range(start,end+1):#判断斜方向胜负（左下右上）
				if self.board[index][s-index][2]==k and k==1:
					count+=1

					if count>=5:
						text.draw("绿色方胜",88,160,0xff0000)
				else:
					count=0
			for index in range(start,end+1):
				if self.board[index][s-index][2]==k and k==2:
					count+=1

					if count>=5:
						text.draw("黑色方胜",88,160,0xff0000)
				else:
					count=0
			
		
	def keyboardEvent(self, key):
        # 右移选择键
		if self.keymatch[key] == "Key1":
            # 取消前一个选择            
			x = self.board[self.selectYi][self.selectXi][0]
			y = self.board[self.selectYi][self.selectXi][1]
			self.drawcross(x, y, 0xffffff)
            # 选择右边一个
			self.selectXi=(self.selectXi+1)%11
			x = self.board[self.selectYi][self.selectXi][0]
			y = self.board[self.selectYi][self.selectXi][1]
			self.drawcross(x, y, 0xff0000)
		# 纵向移动键
		elif self.keymatch[key] == "Key2":
			# 取消前一个选择
			x = self.board[self.selectYi][self.selectXi][0]
			y = self.board[self.selectYi][self.selectXi][1]
			self.drawcross(x, y, 0xffffff)
            # 选择下边一个
			self.selectYi=(self.selectYi+1)%11
			x = self.board[self.selectYi][self.selectXi][0]
			y = self.board[self.selectYi][self.selectXi][1]
			self.drawcross(x, y, 0xff0000)
        # 确认键
		elif self.keymatch[key] == "Key3":
			x = self.board[self.selectYi][self.selectXi][0]
			y = self.board[self.selectYi][self.selectXi][1]
			if self.board[self.selectYi][self.selectXi][2]==0:
				self.put_circle_back(x,y,10,self.color)#画黑色棋子
				self.board[self.selectYi][self.selectXi][2]=2#将棋子标记为黑色
				s=(self.selectYi)*11+(self.selectXi)
				self.d=str(s)
				self.c.publish(self.TOPIC2,self.d)#向服务器发送棋子位置信息
			self.is_win(self.selectXi,self.selectYi,self.board[self.selectYi][self.selectXi][2])
		elif self.keymatch[key] == "Key4":
			self.displayInit()
	def start(self):
		try:
			while True:
				self.c.check_msg()#检查是否收到信息
				i = 0#用来辅助判断那个按键被按下
				j = -1
				for k in self.keys:
					if (k.value() == 0):#如果按键被按下
						if i != j:
							j = i
							self.keyboardEvent(i)#触发相应按键对应事件
					i = i + 1
					if (i > 3):
						i = 0
				time.sleep_ms(200)  # 按键去抖
		finally:
				self.c.disconnect()
				print("MQTT连接断开")

if __name__ == '__main__':
	go = GOES()
	go.do_connect()
	go.esp()
	go.start()