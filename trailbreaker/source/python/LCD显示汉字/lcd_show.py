
import time
import pyb
import font
from font import *
from pyb import Pin

print("start")
class USR_SPI:

  def __init__(self,scl,sda,dc):
    self.scl = scl
    self.sda = sda
    self.dc = dc
  
  def write_u8(self,data):
    for i in range (8): #send data
      if data & (0x80):
        self.sda(1)
        #print(1)
      else:
        self.sda(0)
        #print(0)
      self.scl(0)
      self.scl(1)
      data = data << 1  

    
  def write_data(self,buf):
      self.dc(1) #send 1 for data
      self.write_u8(buf)

  def write_cmd(self,cmd_buf):
      self.dc(0) #send 0 for cmd
      self.write_u8(cmd_buf)

  #def read_data(self,cont):
    #buffer = bytearray(cont-1)
    #self.scl(0)
    #self.scl(1)
    #for i in range (9): #send data
      #self.scl(0)
      #self.scl(1)
    #for i in (0,cont-1)
      #buffer[i] = self.read_byte()
    #return bytes(buffer)
    
 # def read_byte(self):
    
class DISPLAY:
  RED =   0xf800
  GREEN = 0x07e0
  BLUE =  0X001f
  PINK =  0xd2f5
  ORANGE = 0xfd20
  YELLOW = 0xffe0
  BLACK = 0x0000
  WHITE = 0Xffff

  def __init__(self,spi,cs,res,led_en):
    
    self.spi = spi
    self.cs = cs
    self.res = res
    self.led_en=led_en
    self.init()
      
  #液晶的初始化程序
  def init(self):
    self.led_en(1)
    self.cs(0)   #片选使能
    self.res(1)
    pyb.delay(10)
    self.res(0)
    pyb.delay(10)
    self.res(1)
    pyb.delay(150)
    self.spi.write_cmd(0x11)   #唤醒LCD
    pyb.delay(150)
    
    self.spi.write_cmd(0xb1)    #Frame rate
    self.spi.write_data(0x02)
    self.spi.write_data(0x35)
    self.spi.write_data(0x36)
    self.spi.write_cmd(0xb2)
    self.spi.write_data(0x02)
    self.spi.write_data(0x35)
    self.spi.write_data(0x36)
    self.spi.write_cmd(0xb3)
    self.spi.write_data(0x02)
    self.spi.write_data(0x35)

    self.spi.write_data(0x36)
    self.spi.write_data(0x02)
    self.spi.write_data(0x35)
    self.spi.write_data(0x36)
  
    self.spi.write_cmd(0xb4)  #dot inversion
    self.spi.write_data(0x03) 
    
    self.spi.write_cmd(0xc0)  #power sequence
    self.spi.write_data(0xa2) 
    self.spi.write_data(0x02) 
    self.spi.write_data(0x84) 
    self.spi.write_cmd(0xc1)
    self.spi.write_data(0xc5) 
    self.spi.write_cmd(0xc2)
    self.spi.write_data(0x0d) 
    self.spi.write_data(0x00) 
    self.spi.write_cmd(0xc3)
    self.spi.write_data(0x8d) 
    self.spi.write_data(0x2a) 
    self.spi.write_cmd(0xc4)
    self.spi.write_data(0x8d) 
    self.spi.write_data(0xee)
    
    self.spi.write_cmd(0xe0)     #gamma sequence
    self.spi.write_data(0x12)
    self.spi.write_data(0x1c)
    self.spi.write_data(0x10)
    self.spi.write_data(0x18)
    self.spi.write_data(0x33)
    self.spi.write_data(0x2c)
    self.spi.write_data(0x25)
    self.spi.write_data(0x28)
    self.spi.write_data(0x28)
    self.spi.write_data(0x27)
    self.spi.write_data(0x2f)
    self.spi.write_data(0x3c)
    self.spi.write_data(0x00)
    self.spi.write_data(0x03)
    self.spi.write_data(0x03)
    self.spi.write_data(0x10)
    self.spi.write_cmd(0xe1)
    self.spi.write_data(0x12)
    self.spi.write_data(0x1c)
    self.spi.write_data(0x10)
    self.spi.write_data(0x18)
    self.spi.write_data(0x2d)
    self.spi.write_data(0x28)
    self.spi.write_data(0x23)
    self.spi.write_data(0x28)
    self.spi.write_data(0x28)
    self.spi.write_data(0x26)
    self.spi.write_data(0x2f)
    self.spi.write_data(0x3b)
    self.spi.write_data(0x00)
    self.spi.write_data(0x03)
    self.spi.write_data(0x03)
    self.spi.write_data(0x10)
    
    self.spi.write_cmd(0xC5)  #VCOM
    self.spi.write_data(0x0E)
    self.spi.write_cmd(0x36)  #MX,MY,RGB mode
    self.spi.write_data(0xC0)  #0xC0    rgb565

    self.spi.write_cmd(0x3A)  #65k mode 
    self.spi.write_data(0x05)
    self.spi.write_cmd(0x29)  #Display on
  #清屏函数，color为清屏颜色
  def clr(self,clr_color):
    clr_h=(clr_color&0xff00)>>8
    clr_l=clr_color&0x00ff  
    self.spi.write_cmd(0x2A)  
    self.spi.write_data(0x00)
    self.spi.write_data(0x02)
    self.spi.write_data(0x00)
    self.spi.write_data(0x81)

    self.spi.write_cmd(0x2B)
    self.spi.write_data(0x00)
    self.spi.write_data(0x01)
    self.spi.write_data(0x00)
    self.spi.write_data(0xA0)
    self.spi.write_cmd(0x2C)
    for i in range (20480):  #20480
      self.spi.write_data(clr_h)
      self.spi.write_data(clr_l)
  #画点函数，x,y起始做标,屏幕左上角是0,0;
  #屏幕右下角是127,159;color: 特定颜色
  def putpixel(self,x,y,color):
    col_h=(color&0xff00)>>8
    col_l=color&0x00ff
    self.spi.write_cmd(0x2a)
    self.spi.write_data(0x00)
    self.spi.write_data(x+2)
    self.spi.write_cmd(0x2b)
    self.spi.write_data(0x00)
    self.spi.write_data(y+1)
    self.spi.write_cmd(0x2c)
    self.spi.write_data(col_h)
    self.spi.write_data(col_l)
    
  #画矩形函数，x,y为起始点的横纵坐标，x_len,y_len为两个边的长度
  def putrect(self,x,y,x_len,y_len,color):
    #print(12)
    col_h=(color&0xff00)>>8
    col_l=color&0x00ff   
    self.spi.write_cmd(0x2a)  
    self.spi.write_data(0x00)
    self.spi.write_data(0x02+x)
    self.spi.write_data(0x00)
    self.spi.write_data(0x02+x+x_len-1)
    self.spi.write_cmd(0x2b)
    self.spi.write_data(0x00)
    self.spi.write_data(0x01+y)
    self.spi.write_data(0x00)
    self.spi.write_data(0x01+y+y_len-1)
    self.spi.write_cmd(0x2c)
    for i in range ((x_len+1)*(y_len+1)):
      self.spi.write_data(col_h)
      self.spi.write_data(col_l)    
  #显示ASCII码，显示值为20H-7FH(若为其它值，则显示' ')
  #x,y起始做标,屏幕左上角是0,0;屏幕右下角是127,159;
  #ch是字符;color: 特定颜色
  def putchar(self,x,y,ch,color):
    char=ord(ch)    #将字符型转成数字
    if((char<0x20)or(char>0x7f)):
      char=0x20
    char-=0x20
    for i in range(5):#选择对应的ASCII字符
      font_dat = ASCII[char*5+i]
      for j in range(8):
        if(font_dat&0x01<<j):
          self.putpixel(x,y,color)
        y=y+1
      x=x+1  
      y=y-8
  #显示中文字符，字符存在font文件的Chinese中
  #xy为起始坐标,屏幕左上角是0,0;屏幕右下角是127,159;
  def putChinese(self,x,y,color):
    for i in range(3,-1,-1):#4个字符，每个字符内有32个8位二进制数，前16个是左半边的显示，后16个是右半边的显示
      font=Chinese[i]#选择中文字符
      for j in range(16,32):#每个字符16行,先取右半边数值
        font_dat = font[j]#右半边选择一行
        for j in range(8):#开始显示
          if(font_dat&0x01<<j):
            self.putpixel(x,y,color)
          y=y+1#像素右移
        x=x+1  #像素行数下移
        y=y-8#像素右移8格，复位
      #右半边显示完毕，开始显示左半边
      x=x-16#返回第一行
      y=y+8#右侧第一个像素
      for j in range(16):#每个字符16行,取左半边
        font_dat = font[j]#左半边选择一行
        for j in range(8):#开始显示
          if(font_dat&0x01<<j):
            self.putpixel(x,y,color)
          y=y+1#像素右移
        x=x+1  #像素行数下移
        y=y-8#像素右移8格，复位
      #前一个显示完毕，开始显示后一个，y加8，x为同一行
      y=y+8
      x=x-16
  #显示ASCII码，显示值为20H-7FH(若为其它值，则显示' ')   
  #输出显示字符串：x,y起始做标,屏幕左上角是0,0;
  #屏幕右下角是20,16;str是字符串;color: 特定颜色
  def putstr(self,x,y,str,color):
    str_list=list(str) #str change list
    x*=6
    y*=9
    for char in str_list:
      if char == "\n":
        break
      else:
        self.putchar(x,y,char,color)
        x+=6
  #x,y起始做标,屏幕左上角是0,0;屏幕右下角是127,159;
  #ch是字符;color:特定颜色,color_back:背景颜色
  def putchar_back(self,x,y,ch,color,color_back):
    char=ord(ch)
    if((char<0x20)or(char>0x7f)):
      char=0x20
    char-=0x20
    self.putrect(x,y,6,8,color_back)
    for i in range(5):
      font_dat = ASCII[char*5+i]
      for j in range(8):
        if(font_dat&0x01<<j):
          self.putpixel(x,y,color)
        y=y+1
      x=x+1  
      y=y-8
  #x,y起始行列做标,屏幕左上角是0,0;屏幕右下角是20,16;
  #str是字符串;color:特定颜色,color_back:背景颜色
  def putstr_back(self,x,y,str,color,color_back):
    str_list=list(str) #str change list
    x*=6
    y*=9  
    for char in str_list:
      if char == "\n":
        break
      else:
        self.putchar_back(x,y,char,color,color_back)
        x+=6    
  #画水平线函数：x,y起始做标,屏幕左上角是0,0;
  #屏幕右下角是127,159;len是长度;color: 特定颜色   
  def put_hline(self,x,y,len,color):
    col_h=(color&0xff00)>>8
    col_l=color&0x00ff   
    self.spi.write_cmd(0x2a)  
    self.spi.write_data(0x00)
    self.spi.write_data(0x02+x)
    self.spi.write_data(0x00)
    self.spi.write_data(0x02+x+len)
    self.spi.write_cmd(0x2b)
    self.spi.write_data(0x00)
    self.spi.write_data(0x01+y)
    self.spi.write_data(0x00)
    self.spi.write_data(0x01+y)
    self.spi.write_cmd(0x2c)
    for i in range (len):
      self.spi.write_data(col_h)
      self.spi.write_data(col_l)    
  #画垂直线函数：x,y起始做标,屏幕左上角是0,0;
  #屏幕右下角是127,159;len是长度;color: 特定颜色
  def put_vline(self,x,y,len,color):
    col_h=(color&0xff00)>>8
    col_l=color&0x00ff   
    self.spi.write_cmd(0x2a)  
    self.spi.write_data(0x00)
    self.spi.write_data(0x02+x)
    self.spi.write_data(0x00)
    self.spi.write_data(0x02+x)
    self.spi.write_cmd(0x2b)
    self.spi.write_data(0x00)
    self.spi.write_data(0x01+y)
    self.spi.write_data(0x00)
    self.spi.write_data(0x01+y+len)
    self.spi.write_cmd(0x2c)
    for i in range (len):
      self.spi.write_data(col_h)
      self.spi.write_data(col_l)    
  #画圆函数：x,y为圆心坐标，r为圆的半径，color为指定颜色
  def put_circle(self,x,y,r,color):
    a=0
    b=r
    di=3-(r<<1)
    while (a<=b):
      self.putpixel(x-b,y-a,color)
      self.putpixel(x+b,y-a,color)
      self.putpixel(x-a,y+b,color)
      self.putpixel(x-b,y-a,color)
      self.putpixel(x-a,y-b,color)
      self.putpixel(x+b,y+a,color)
      self.putpixel(x+a,y-b,color)
      self.putpixel(x+a,y+b,color)
      self.putpixel(x-b,y+a,color)
      a+=1
      if(di<0):
        di+=4*a+6
      else:
        di+=10+4*(a-b)
        b-=1
      self.putpixel(x+a,y+b,color)
  
  def cloth(self,x,y,color):
    #print(12)
    self.put_hline(x,y+6,4,color)
    self.put_vline(x+4,y+4,3,color)
    self.put_hline(x+4,y+4,7,color)
    self.put_hline(x+10,y+5,1,color)
    self.put_hline(x+9,y+6,6,color)
    self.put_hline(x+14,y+7,1,color)
    self.put_hline(x+9,y+8,6,color)
    self.put_hline(x+14,y+9,1,color)
    self.put_hline(x+9,y+10,6,color)
    self.put_hline(x+14,y+11,1,color)
    self.put_hline(x+9,y+12,6,color)
    self.put_hline(x+14,y+13,1,color)
    self.put_hline(x+3,y+14,11,color)
    self.put_hline(x,y+13,3,color)


  def stone(self,x,y,color):
    #print(12)
    self.put_hline(x,y+6,4,color)
    self.put_vline(x+4,y+4,3,color)
    self.put_hline(x+4,y+4,7,color)
    self.put_hline(x+10,y+5,1,color)
    self.put_hline(x+9,y+6,3,color)
    self.put_hline(x+11,y+7,1,color)
    self.put_hline(x+9,y+8,3,color)
    self.put_hline(x+11,y+9,1,color)
    self.put_hline(x+9,y+10,3,color)
    self.put_hline(x+11,y+11,1,color)
    self.put_hline(x+9,y+12,3,color)
    self.put_hline(x+11,y+13,1,color)
    self.put_hline(x+3,y+14,8,color)
    self.put_hline(x,y+13,3,color)
	
	
  def scissor(self,x,y,color):
    #print(12)
    self.put_hline(x,y+6,4,color)
    self.put_vline(x+4,y+4,3,color)
    self.put_hline(x+4,y+4,7,color)
    self.put_hline(x+10,y+5,1,color)
    self.put_hline(x+9,y+6,6,color)
    self.put_hline(x+14,y+7,1,color)
    self.put_hline(x+9,y+8,6,color)
    self.put_hline(x+14,y+9,1,color)
    self.put_hline(x+9,y+10,6,color)
    self.put_vline(x+9,y+11,4,color)
    self.put_hline(x+3,y+14,7,color)
    self.put_hline(x,y+13,3,color)


print("end")







