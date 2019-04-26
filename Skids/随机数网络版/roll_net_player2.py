'''
本程序为二号玩家，发送的数据为字符串型21-26
首位2代表二号玩家，第二位代表选择
一号玩家的首位为1，第二位和本程序相同
'''
from machine import Pin,UART
import random
import time
import screen
import ubitmap
import text
import network
import utime
from random import randint
from umqtt.simple import MQTTClient

screen.clear()


pins = [36,39,34,35]
keys = []
for p in pins:
    keys.append(Pin(p,Pin.IN))


class Game():
  def __init__(self, playerName, computerName):#初始化
    #网络设定
    #WiFi名称和密码
    self.wifi_name = "NEUI"
    self.wifi_SSID = "NEUI3187"
    #MQTT服务端信息
    SERVER = "112.125.89.85"   #MQTT服务器地址
    SERVER_PORT = 3881         #MQTT服务器端口
    DEVICE_ID = "wc001"        #设备ID
    TOPIC1 = b"/cloud-skids/online/dev/" + DEVICE_ID
    self.TOPIC2 = b"/cloud-skids/message/server/" + DEVICE_ID
    CLIENT_ID = "f25410646a8348f8a1726a3890ad8f82"
    #设备状态
    ON = "1"
    OFF = "0"
    #对方的选择
    self.d=["1","2","3"]
    self.choose=0
    self.mark=0
    #启动网络连接
    self.do_connect()
    gc.collect()
    self.client = MQTTClient(CLIENT_ID, SERVER, SERVER_PORT)
    self.client.set_callback(self.sub_cb)    #设置回调
    self.client.connect()
    print("连接到服务器：%s" % SERVER)
    self.client.publish(TOPIC1, ON)     #发布“1”到TOPIC1
    self.client.subscribe(self.TOPIC2)       #订阅TOPIC
    #游戏设定
    self.gameStart = False
    self.playerName = playerName
    self.computerName = computerName
    self.playerScore = 0
    self.computerScore = 0
    self.equalNum = 0
    self.playerStatus = 0;
    self.computerStatus = 0
    for p in pins:
      keys.append(Pin(p,Pin.IN))
    self.displayInit()
    
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
    
    

      
      
  def sub_cb(self,topic, message):
    message = message.decode()
    print("mark is :",self.mark)
    #赋值给choose
    self.choose=int(message)

    if (self.choose>20 ):#来自2号自己的信息，不判断
      print ("对方尚未选择")
      return
    elif(self.choose<20):
      self.mark=self.mark+1#修改标志，代表一方已完成选择
      print("player2 get choose is :",self.choose)
      #处理所得信息
      self.computerStatus = self.choose-10
      #显示对方结果
      text.draw(str(self.computerStatus), 172, 152, 0x000000, 0xffffff)
    #判断胜负并显示结果
    if self.mark%2==0:#如果双方都完成选择
      resultMessage = " 平局 "
      if self.computerStatus==0:
        return
      elif(self.playerStatus==self.computerStatus):
        self.equalNum+=1
      elif(self.playerStatus>self.computerStatus):
        self.playerScore+=1
        resultMessage = "%s胜出"%self.playerName
      elif(self.playerStatus<self.computerStatus):
        self.computerScore+=1
        resultMessage = "%s胜出"%self.computerName
      text.draw(resultMessage, 90, 210, 0x000000, 0xffffff)
      self.updateTotolArea()

  def displayInit(self, x=10, y=10, w=222, h=303):
    #显示游戏规则信息
    mentionStr1 = "游戏规则："
    mentionStr2 = "双方随机生成1-6的数"
    mentionStr3 = "按键1-3选择 按键4停止"
    text.draw(mentionStr1, 20, 20, 0x000000, 0xffffff)
    text.draw(mentionStr2, 20, 36, 0x000000, 0xffffff)
    text.draw(mentionStr3, 20, 52, 0x000000, 0xffffff)
    text.draw("-------------", 20, 68, 0x000000, 0xffffff)
    self.updateTotolArea()
    #设置游戏运行状态
    self.gameStart = True
    
    
  def roll(self):
    #获得随机数并更新显示
    result1=randint(1,6)
    text.draw(str(result1), 52, 152, 0x000000, 0xffffff)
    self.playerStatus=result1
    
  def pressKeyboardEvent(self, key):
    keymatch=["Key1","Key2","Key3","Key4"]
    #游戏还未开始，不必处理键盘输入
    if(self.gameStart == False):
      return
    #处理按键
    print(keymatch[key])
    self.mark=self.mark+1
    if(keymatch[key] == "Key1"):
      self.roll()
      self.client.publish(self.TOPIC2,"2"+str(self.playerStatus))
      text.draw(str(self.playerStatus), 52, 168, 0x000000, 0xffffff)
    elif(keymatch[key] == "Key2"):
      self.roll()
      self.client.publish(self.TOPIC2,"2"+str(self.playerStatus))
      text.draw(str(self.playerStatus), 52, 168, 0x000000, 0xffffff)
    elif(keymatch[key] == "Key3"):
      self.roll()
      self.client.publish(self.TOPIC2,"2"+str(self.playerStatus))
      text.draw(str(self.playerStatus), 52, 168, 0x000000, 0xffffff)
    else:
      text.draw("游戏结束", 90, 210, 0x000000, 0xffffff)
      #设置游戏运行状态
      self.gameStart = False
      return

    #对方玩家选择

    #二号玩家收到11-16

    print("choose is :",self.choose)
    if (self.choose>20 ):#来自2号自己的信息，不判断
      print ("对方尚未选择")
      return
    elif(self.choose<20):
      print("player1 get choose is :",self.choose)
      #处理所得信息
      self.computerStatus = self.choose-10
      #显示对方结果
      text.draw(str(self.computerStatus), 172, 152, 0x000000, 0xffffff)
    
    #判断胜负并显示结果
    if self.mark%2==0:#如果双方都完成选择
      resultMessage = " 平局 "
      if self.computerStatus==0:
        return
      elif(self.playerStatus==self.computerStatus):
        self.equalNum+=1
      elif(self.playerStatus>self.computerStatus):
        self.playerScore+=1
        resultMessage = "%s胜出"%self.playerName
      elif(self.playerStatus<self.computerStatus):
        self.computerScore+=1
        resultMessage = "%s胜出"%self.computerName
      text.draw(resultMessage, 90, 210, 0x000000, 0xffffff)
      self.updateTotolArea()

  
  

  
  
  def startGame(self): 

    print("-------骰子游戏开始-------")
    while True:
      self.client.check_msg()
      self.roll()
      #print(gc.mem_free())
      i = 0
      j = -1
      for k in keys:
        if(k.value() == 0):
          if i!=j:
            j = i
            
            self.pressKeyboardEvent(i)
            self.client.check_msg()
        i = i+1;
        if(i > 3):
          i = 0
      time.sleep_ms(100)#按键防抖
    
  def updateTotolArea(self):
    #汇总区域用于显示电脑和玩家的胜平负次数
    print("-------更新汇总区域-------")
    playerTotal = "%s赢了%d局" % (self.playerName, self.playerScore)
    computerTotal = "%s赢了%d局" % (self.computerName, self.computerScore)
    equalTotal = "平局%d次" % self.equalNum
    text.draw("-------------", 20, 240, 0x000000, 0xffffff)
    text.draw(playerTotal, 20, 256, 0x000000, 0xffffff)
    text.draw(computerTotal, 20, 272, 0x000000, 0xffffff)
    text.draw(equalTotal, 20, 288, 0x000000, 0xffffff)

if __name__ == '__main__':
    newGame = Game("玩家2", "玩家1")
    newGame.startGame()

