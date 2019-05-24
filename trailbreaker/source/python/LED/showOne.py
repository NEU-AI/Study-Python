from pyb import Pin

r=[Pin(i, Pin.OUT_PP) for i in ['X2','X1','X3','X4','X5','X6','X8','X7']]
for i in range (8):
    r[i].high()

c=[Pin(i, Pin.OUT_PP) for i in ['Y2','Y1','Y3','Y4','Y5','Y6','Y8','Y7']]
for i in range (8):
    c[i].high()

def ledDemo1(): #点亮1个
    r[0].low()
    c[0].low()

def ledDemo2(): #第一行点亮
    for j in range(8):
        c[j].low()

    r[0].low()
	
def ledDemo3(): #一行逐个点亮
    r[0].low()         #MOS开关闭合
    for j in range(8): #列循环
        c[j].low()     #点亮 
        pyb.delay(100) #延时
        c[j].high()    #熄灭
    r[0].high()        #MOS开关断开

def ledDemo4(): #逐个点亮
    for i in range(8):     #行循环
        r[i].low()         #MOS开关闭合
        for j in range(8): #列循环
            c[j].low()     #点亮 
            pyb.delay(100) #延时
            c[j].high()    #熄灭
        r[i].high()        #MOS开关断开
def ledDemo5(): #逐行点亮
    for j in range(8):
        c[j].low()

    for i in range(8):
        r[i].low()
        pyb.delay(500)
        r[i].high()

def ledDemo6(): #全部点亮
    for k in range(300):
        for j in range(8):
            c[j].low()

        for i in range(8):
            r[i].low()
            pyb.delay(2)
            r[i].high()
    for j in range(8):
        c[j].high()
#显示字母R
def ledDemo7(): 
    for k in range(300):
        line(1,[])
        line(2,[2,3,4,5])
        line(3,[2,6])
        line(4,[2,3,4,5])
        line(5,[2,3])
        line(6,[2,4])
        line(7,[2,5])
        line(8,[2,6]) 

#显示一行
def line(row,colDisp):
    r[row-1].low()
    for j in colDisp:
        c[j].low()
        pyb.delay(1)
        c[j].high()
    r[row-1].high()
ledDemo1() 

