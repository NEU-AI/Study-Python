from pyb import Pin

r=[Pin(i, Pin.OUT_PP) for i in ['X2','X1','X3','X4','X5','X6','X8','X7']]
for i in range (8):
    r[i].high()

c=[Pin(i, Pin.OUT_PP) for i in ['Y2','Y1','Y3','Y4','Y5','Y6','Y8','Y7']]
for i in range (8):
    c[i].high()

'''
def move():
	for j in range(8):#从一行开始
		r[j].low()#对第一行，读每一列，之后全部左移
		for i in range(1,7): #读1-7列
			if(!Pin.value(c[j])):#后一列LED为亮，则前一列也为亮
				c[j-1].low()
				pyb.delay(1)
				c[j-1].high()
			else:
				c[j-1].high()#后一列为灭，则前一列也为灭
	#全部行都左移完毕，函数结束
	
'''	


r[1].low()         #开启第一行
c[1].low()     #开启第一列，此时位于第一行第一列的灯亮起
pyb.delay(1000) #延时1s
c[1].high()    #熄灭
r[1].high()        #关闭第一行
pyb.delay()
r[1].low()         #开启第一行
c[1].low()     #开启第一列，此时位于第一行第一列的灯亮起
pyb.delay(1000) #延时1s
c[1].high()    #熄灭
r[1].high()        #关闭第一行

for i in range(100):
	r[1].low()        
	c[1].low()     
	pyb.delay(300) 
	c[1].high()    
	r[1].high()      

def ledDemo1(): #逐个点亮
    for i in range(8):     #行循环
        r[i].low()         #MOS开关闭合
        for j in range(8): #列循环
            c[j].low()     #点亮
            pyb.delay(100) #延时
            c[j].high()    #熄灭
        r[i].high()        #MOS开关断开

def ledDemo2(): #逐行点亮
    for j in range(8):
        c[j].low()#打开全部的列

    for i in range(8):#开始显示行，从上到下
        r[i].low()
        pyb.delay(500)
        r[i].high()

def ledDemo3(): #全部点亮
    for k in range(300):#持续时间
        for j in range(8):#打开全部列
            c[j].low()

        for i in range(8):#以2ms的间隔进行快速变换
            r[i].low()
            pyb.delay(2)
            r[i].high()
    for j in range(8):#关闭列
        c[j].high()       

#显示一行
def line(row,colDisp):
    r[row-1].low() #打开某行
    for j in colDisp: 
        c[j].low()#开启
        pyb.delay(1)
        c[j].high()#熄灭
    r[row-1].high()#关闭列

#显示字母R
def ledDemo4(): 
    for k in range(300):
        line(1,[])
        line(2,[2,3,4,5])
        line(3,[2,6])
        line(4,[2,3,4,5])
        line(5,[2,3])
        line(6,[2,4])
        line(7,[2,5])
        line(8,[2,6]) 
		

		
		
		
		
		
def show_R(): 
    for k in range(300):
        line(1,[])
        line(2,[2,3,4,5])
        line(3,[2,6])
        line(4,[2,3,4,5])
        line(5,[2,3])
        line(6,[2,4])
        line(7,[2,5])
        line(8,[2,6])

def show_0(): 
    for k in range(300):
        line(1,[])
        line(2,[2,3,4])
        line(3,[1,5])
        line(4,[1,5])
        line(5,[1,5])
        line(6,[1,5])
        line(7,[2,3,4])
        line(8,[])

def show_1(): 
    for k in range(300):
        line(1,[])
        line(2,[3,4])
        line(3,[2,3,4])
        line(4,[3,4])
        line(5,[3,4])
        line(6,[3,4])
        line(7,[3,4])
        line(8,[])	
		
def show_2(): 
    for k in range(300):
        line(1,[])
        line(2,[2,3,4,5])
        line(3,[1,2,5,6])
        line(4,[1,5,6])
        line(5,[4,5])
        line(6,[3,4])
        line(7,[1,2,3,4,5,6])
        line(8,[])			

def show_3(): 
    for k in range(300):
        line(1,[3,4,5])
        line(2,[2,6])
        line(3,[6])
        line(4,[3.4,5,6])
        line(5,[5])
        line(6,[6])
        line(7,[2,6])
        line(8,[3,4,5])
def show_A(): 
    for k in range(300):
        line(1,[3,4])
        line(2,[3,4])
        line(3,[2,5])
        line(4,[2,5])
        line(5,[1,2,3,4,5,6])
        line(6,[1,6])
        line(7,[0,7])
        line(8,[])

def show_B(): 
    for k in range(300):
        line(1,[1,2,3,4])
        line(2,[1,5])
        line(3,[1,5])
        line(4,[1,2,3,4])
        line(5,[1,5])
        line(6,[1,5])
        line(7,[1,5])
        line(8,[1,2,3,4])

def show_C(): 
    for k in range(300):
        line(1,[2,3,4])
        line(2,[1,5])
        line(3,[1,5])
        line(4,[1])
        line(5,[1])
        line(6,[1,5])
        line(7,[1,5])
        line(8,[2,3,4])

def show_D(): 
    for k in range(300):
        line(1,[1,2,3])
        line(2,[1,4])
        line(3,[1,5])
        line(4,[1,5])
        line(5,[1,5])
        line(6,[1,5])
        line(7,[1,4])
        line(8,[1,2,3])

while True:
	ledDemo1()
	ledDemo2()
	ledDemo3()
	ledDemo4()
	show_0()
	show_1()
	show_2()
	show_3()
	show_A()
	show_B()
	show_C()
	show_D()