# main.py -- put your code here!
import pyb
from pyb import Pin

# 获取引脚
Pin_All=[Pin(p,Pin.OUT_PP) for p in ['X2','X1','X3','X4']]

# 转速(ms) 数值越大转速越慢，最小值为1.8ms
speed=3

STEPER_ROUND=512  #转动一圈(360度)所需的周期数
ANGLE_PER_ROUND=STEPER_ROUND/360  #转动1度所需的周期数

# 引脚控制脉冲函数，一个周期
def SteperWriteData(data):
    count=0
    for i in data:
        Pin_All[count].value(i)
        count+=1

# 电机转动函数，通过双四拍驱动，每拍延迟speed毫秒
def SteperFrontTurn():
    global speed
    
    SteperWriteData([0,0,1,1])
    pyb.delay(speed)

    SteperWriteData([1,0,0,1])
    pyb.delay(speed)

    SteperWriteData([1,1,0,0])
    pyb.delay(speed)
    
    SteperWriteData([0,1,1,0])   
    pyb.delay(speed)

# 电机停转函数
def SteperStop():
    SteperWriteData([0,0,0,0])
	
# 控制旋转角度函数，传入参数angle为要旋转的角度
def SteperRun(angle):
    global ANGLE_PER_ROUND #旋转1度需要的周期数  
    val=ANGLE_PER_ROUND*abs(angle) #总共需要的周期数
    for i in range(0,val):
        SteperFrontTurn()
    angle = 0
    SteperStop()

# 设定要旋转的角度开始驱动步进电机转动
if __name__=='__main__':
    SteperRun(180) #旋转180度，可以设置任意度数
