from pyb import Pin,Timer
import lcd_show
from lcd_show import *
import pyb
from pyb import Pin

#LCD
usrspi = USR_SPI(scl=Pin('X6',Pin.OUT_PP), sda=Pin('X7', Pin.OUT),dc=Pin('X8', Pin.OUT))
disp = DISPLAY(usrspi,cs=Pin('X5', Pin.OUT),res=Pin('X4', Pin.OUT),led_en=Pin('X3', Pin.OUT))
x1 = Pin('X3',Pin.OUT_PP)
R=[Pin('X9',Pin.OUT_PP),Pin('X10',Pin.OUT_PP),Pin('Y3',Pin.OUT_PP),Pin('Y4',Pin.OUT_PP)]
C=[Pin('Y5',Pin.IN,Pin.PULL_UP),Pin('Y6',Pin.IN,Pin.PULL_UP),Pin('Y8',Pin.IN,Pin.PULL_UP),Pin('Y7',Pin.IN,Pin.PULL_UP)]
formu=["0"]
fir=0
sec=0

def transfer(number):
	#print(number)
	value1=0
	value2=0
	tag=0
	#print(len(number))
	for i in range(len(number)):
		if number[i]==".":#有小数
			tag=1
			for j in range(i):
				value1+=float(number[j])*pow(10,i-1-j)
			for j in range(i+1,len(number)):
				value1+=float(number[j])*pow(10,i-j)
	if tag==1:
		return value1
	for k in range(len(number)):
		value2+=float(number[k])*pow(10,len(number)-1-k)
	return value2
	
'''
def compute():
	global formu,fir,sec
	print (formu)
	for i in range(len(formu)):
		if ((formu[i]=="+") or (formu[i]=="-") or (formu[i]=="*") or (formu[i]=="/")):
			fir=formu[0:i]
			sec=formu[i+1:len(formu)-1]
			a=transfer(fir)
			b=transfer(sec)
			if formu[i]=="+":
				value=a+b
				return value
			if formu[i]=="-":
				value=a-b
				return value
			if formu[i]=="*":
				value=a*b
				return value
			if formu[i]=="/":
				value=a/b
				return value
remove=0
'''
remove=0
disp.clr(disp.PINK)
key=1
mark=0#加减乘除
place=0#当前字符所在位置
operator=0#运算符位置
while True:#扫描键盘
	for i in range(0,4):
		R[i].low()
		for k in range(0,4):
			if k!=i:
				R[k].high()
		for j in range(0,4):
			if i==0 and j==0 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('7')
				formu+="7"
				place=place+1
			elif i==0 and j==1 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('8')
				formu+="8"
				place=place+1
			elif i==0 and j==2 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('9')
				formu+="9"
				place=place+1
			elif i==0 and j==3 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('/')
				formu+="/"
				place=place+1
			elif i==1 and j==0 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('4')
				formu+="4"
				place=place+1
			elif i==1 and j==1 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('5')
				formu+="5"
				place=place+1
			elif i==1 and j==2 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('6')
				formu+="6"
				place=place+1
			elif i==1 and j==3 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('*')
				formu+="*"
				place=place+1
			elif i==2 and j==0 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('1')
				formu+="1"
				place=place+1
			elif i==2 and j==1 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('2')
				formu+="2"
				place=place+1
			elif i==2 and j==2 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('3')
				formu+="3"
				place=place+1
			elif i==2 and j==3 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('-')
				formu+="-"
				place=place+1
			elif i==3 and j==0 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('0')
				formu+="0"
				place=place+1
			elif i==3 and j==1 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('.')
				formu+="."
				place=place+1
			elif i==3 and j==2 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('=')
				formu+="="
				place=place+1
			elif i==3 and j==3 and C[j].value()==0:
				pyb.delay(10)
				#if C[j].value()==0:
				print('+')
				formu+="+"
				place=place+1
		pyb.delay(50)
	if len(formu)>1:
		if (((formu[0]=="+") or (formu[0]=="-") or (formu[0]=="*") or (formu[0]=="/")) and len(formu)>1):
			formu=formu[1:]
			#print("formu more than len 1 is " ,end=" ")
			#print(formu)
		if (((formu[-1]=="+") or (formu[-1]=="-") or (formu[-1]=="*") or (formu[-1]=="/") or (formu[-1]=="=")) and len(formu)>=1):
			#print("formu out loop  is " ,end=" ")
			#print(formu)
			#print("remove  is " ,end=" ")
			#print(remove)
			operator=place
			if remove==0:
				formu=formu[1:]
				remove=remove+1
			if key ==1:
				fir=transfer(formu[0:operator-1])#翻译第一个数
				print("fir  is : ",end=" ")
				print(fir)
				disp.putstr(6,5,str(fir),0x0000)
				if formu[operator-1]=="+":
					mark=0
					disp.putstr(4,6,"+",0x0000)
				if formu[operator-1]=="-":
					mark=1
					disp.putstr(4,6,"-",0x0000)
				if formu[operator-1]=="*":
					mark=2
					disp.putstr(4,6,"*",0x0000)
				if formu[operator-1]=="/":
					mark=3
					disp.putstr(4,6,"/",0x0000)
				formu=list(formu[-1])
				#print("formu 1 is " ,end=" ")
				#print(formu)
				#disp.putstr(6,5,formu,0xf0f0)
				key=key+1#找到第一个数
				#print("key  is " ,end=" ")
				#print(key)
				#key=key+1
			else :#不是第一个数
				#print("formu 2 is " ,end=" ")
				#print(formu)
				sec=transfer(formu[:-1])
				print("sec  is : ",end=" ")
				print(sec)
				
				disp.putstr(6,6,str(sec),0x0000)
				if mark==0:
					fir=fir+sec
				if mark ==1:
					fir=fir-sec
				if mark==2:
					fir=fir*sec
				if mark==3:
					fir=fir/sec
				if len(formu)>=1:
					if formu[-1]=="+":
						mark=0
					if formu[-1]=="-":
						mark=1
					if formu[-1]=="*":
						mark=2
					if formu[-1]=="/":
						mark=3
					formu=formu[-1]
	if (len(formu)>=1 and formu[-1]=="="):
		print(fir)
		disp.putstr(6,7,str(fir),0x0000)

