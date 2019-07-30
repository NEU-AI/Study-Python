import pyb
from pyb import UART
from pyb import Pin
import time
import utime
from random import randint
import framebuf

class DHT11:#定义DHT11类
    def __init__(self,pin_):#初始化
        #self.data=[]
        self.PinName=pin_
        time.sleep(1)
        self.N1 = Pin(pin_, Pin.OUT_PP)
        #start work
        #N2.low()
        pyb.delay(10)
    def read_temps(self):#读取温度
        data=[]
        j=0
        N1 = Pin(self.PinName, Pin.OUT_PP)#设置输出模式
        #N1=self.N1
        N1.low()#拉低引脚
        time.sleep_ms(20)#保持20ms(最少18ms）
        N1.high()#拉高引脚
        time.sleep_us(30)#保持30us(20~40us）
        #wait to response
        N1 = Pin(self.PinName,Pin.IN)#设置输入模式
        while N1.value()==1:#等待温度传感器响应
            continue
        while N1.value()==0:
            continue
        while N1.value()==1:
            continue
        #get data
        while j<40:#通过引脚接收数据
            k=0
            while N1.value()==0:
                continue
            while N1.value()==1:
                k+=1
                if k>100:break
            if k<3:
                data.append(0)
            else:
                data.append(1)
            j=j+1
        print('Sensor is working')
		#print(k)
        j=0
        #get temperature
		#利用接收的电平信号算出温湿度数值
        humidity_bit=data[0:7]#0-7位湿度信息
        humidity_point_bit=data[8:15]#8-15位湿度小数信息
        temperature_bit=data[16:23]#16-23位温度信息
        temperature_point_bit=data[24:31]#24-31位温度小数信息
        check_bit=data[32:39]#32-39位校验信息
        humidity=0
        humidity_point=0
        temperature=0
        temperature_point=0
        check=0
        for i in range(7):#计算温湿度
            humidity+=humidity_bit[i]*2**(7-i)
            humidity_point+=humidity_point_bit[i]*2**(7-i)
            temperature+=temperature_bit[i]*2**(7-i)
            temperature_point+=temperature_point_bit[i]*2**(7-i)
            check+=check_bit[i]*2**(7-i)
        tmp=humidity+humidity_point+temperature+temperature_point
        if check==tmp:#检验正确，输出结果
            print('temperature is',temperature,'wet is',humidity,'%')
        else:#检验错误，输出数据结果
            print('SHUJUCUOWU',humidity,humidity_point,temperature,temperature_point,check)
        return str(temperature)+','+str(humidity)
while 1:
    S=DHT11('X12')#将Y4引脚传入DHT11类循环测量温湿度数值
    A=S.read_temps()
    pyb.delay(100)
