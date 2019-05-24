from machine import Pin
import random
import time
import screen
import ubitmap
import text

screen.clear()

bmp_shitou = ubitmap.Bitmap("shitou")
bmp_jiandao = ubitmap.Bitmap("jiandao")
bmp_bu = ubitmap.Bitmap("bu")

pins = [36,39,34,35]
keys = []

class Game():
  def __init__(self, playerName, computerName):
    self.gameStart = False
    self.playerName = playerName
    self.computerName = computerName
    self.playerScore = 0
    self.computerScore = 0
    self.equalNum = 0
    self.playerStatus = 0;
    self.playerMessage = ""
    self.computerStatus = 0
    self.computerMessage = ""
    for p in pins:
      keys.append(Pin(p,Pin.IN))
    self.displayInit()
    
  def displayInit(self, x=10, y=10, w=222, h=303):
    #显示游戏规则信息
    mentionStr1 = "游戏规则："
    mentionStr2 = "按键1.剪刀 按键2.石头"
    mentionStr3 = "按键3.布  按键4.结束"
    text.draw(mentionStr1, 20, 20, 0x000000, 0xffffff)
    text.draw(mentionStr2, 20, 36, 0x000000, 0xffffff)
    text.draw(mentionStr3, 20, 52, 0x000000, 0xffffff)
    text.draw("-------------", 20, 68, 0x000000, 0xffffff)
    self.updateTotolArea()
    #设置游戏运行状态
    self.gameStart = True
    
  def pressKeyboardEvent(self, key):  
    keymatch=["Key1","Key2","Key3","Key4"]
    #游戏还未开始，不必处理键盘输入
    if(self.gameStart == False):
      return
    
    print(keymatch[key])
    if(keymatch[key] == "Key1"):
      self.playerStatus = 1
      self.playerMessage = "%s出拳为：剪刀"%self.playerName
      bmp_jiandao.draw(40, 140)
    elif(keymatch[key] == "Key2"):
      self.playerStatus = 2
      self.playerMessage = "%s出拳为：石头"%self.playerName
      bmp_shitou.draw(40, 140)
    elif(keymatch[key] == "Key3"):
      self.playerStatus = 3
      self.playerMessage = "%s出拳为：布 "%self.playerName
      bmp_bu.draw(40, 140)
    else:
      text.draw("游戏结束", 90, 210, 0x000000, 0xffffff)
      #设置游戏运行状态
      self.gameStart = False
      return
    
    #电脑的出拳为一个随机值 
    self.computerStatus = random.randint(1,3)
    print(self.computerStatus)   
    if(self.computerStatus == 1):
      self.computerMessage = "%s出拳为：剪刀"%self.computerName
      bmp_jiandao.draw(150, 140)
    if(self.computerStatus == 2):
      self.computerMessage = "%s出拳为：石头"%self.computerName
      bmp_shitou.draw(150, 140)
    if(self.computerStatus == 3):
      self.computerMessage = "%s出拳为：布 "%self.computerName
      bmp_bu.draw(150, 140)
    
    #显示电脑和玩家的出拳信息
    text.draw(self.playerMessage, 20, 84, 0x000000, 0xffffff)
    text.draw(self.computerMessage, 20, 100, 0x000000, 0xffffff)
    
    #判断胜负并显示结果
    resultMessage = " 平局 "
    if(self.playerStatus == self.computerStatus):
      self.equalNum+=1
    elif(self.playerStatus==1 and self.computerStatus==3):
      resultMessage = "%s胜出"%self.playerName
      self.playerScore+=1
    elif(self.playerStatus==2 and self.computerStatus==1):
      resultMessage = "%s胜出"%self.playerName
      self.playerScore+=1
    elif(self.playerStatus==3 and self.computerStatus==2):
      resultMessage = "%s胜出"%self.playerName
      self.playerScore+=1
    else:
      resultMessage = "%s胜出"%self.computerName
      self.computerScore+=1
    
    text.draw(resultMessage, 90, 210, 0x000000, 0xffffff)
    self.updateTotolArea()
    
  def startGame(self): 
    print("-------猜拳游戏开始-------")
    while True:
      i = 0
      j = -1
      for k in keys:
        if(k.value() == 0):
          if i!=j:
            j = i
            self.pressKeyboardEvent(i)
        i = i+1;
        if(i > 3):
          i = 0
      time.sleep_ms(50)
    
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
    newGame = Game("玩家", "电脑")
    newGame.startGame()

