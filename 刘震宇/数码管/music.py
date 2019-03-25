import pyb
from pyb import Pin,Timer

L1=262 # c 
L2=294 # d 
L3=330 # e 
L4=349 # f 
L5=392 # g 
L6=440 # a1 
L7=494 # b1 

# 定义中音音名
M1=523 # c1 
M2=587 # d1 
M3=659 # e1 
M4=698 # f1
M5=784 # g1 
M6=880 # a2 
M7=988 # b2 

# 定义高音音名
H1=1047 # c2 
H2=1175 # d2 
H3=1319 # e2 
H4=1397 # f2 
H5=1568 # g2 
H6=1760 # a3 
H7=1976 # b3 

# 定义时值单位，决定演奏速度（数值单位：ms） 
T=3600 

MyScore = [[L3, T/4], [L5, T/8+T/16], [L6, T/16], [M1, T/8+T/16], [M2, T/16], [L6, T/16], [M1, T/16],[L5, T/8], [M5, T/8+T/16], [H1, T/16],[M6, T/16], [M5, T/16], [M3, T/16], [M5, T/16], [M2, T/2], [ 1, 1] ]
# 省略后续乐曲数据，请感兴趣的读者补充完整
# 结束 
i=0



def music():
	global i
	x1 = Pin('X3',Pin.OUT_PP)
	tm3=Timer(2, freq=MyScore[i][0])
	led3=tm3.channel(3, Timer.PWM, pin=x1,pulse_width_percent=50)
	a=Pin.value(x1)
	while i<16:
		print(MyScore[i][0])
		tm3.freq(MyScore[i][0])
		pyb.delay(int(MyScore[i][1]))
		i=(i+1)%15
		
#music()
