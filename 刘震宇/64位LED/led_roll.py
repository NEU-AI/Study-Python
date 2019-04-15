from pyb import Pin

r=[Pin(i, Pin.OUT_PP) for i in ['X2','X1','X3','X4','X5','X6','X8','X7']]
for i in range (8):
    r[i].high()

c=[Pin(i, Pin.OUT_PP) for i in ['Y2','Y1','Y3','Y4','Y5','Y6','Y8','Y7']]
for i in range (8):
    c[i].high()
u1=Pin('X9',Pin.IN,Pin.PULL_UP)
u2=Pin('X10',Pin.IN,Pin.PULL_UP)
#显示一行
def line(row,colDisp):
    r[row-1].low() #打开某行
    for j in colDisp: 
        c[j].low()#开启
        pyb.delay(1)
        c[j].high()#熄灭
    r[row-1].high()#关闭列


png1=[
	"0*0000*0",
	"0*0000*0",
	"0*0000*0",
	"0*0000*0",
	"000*0*00",
	"0000*000",
	"000*0*00",
	"00000000"
]
png2=[
	"00000000",
	"00*****0",
	"00*****0",
	"00*****0",
	"00*****0",
	"00*****0",
	"000***00",
	"00000000"
]
png3=[
	"00000000",
	"000*0000",
	"00***000",
	"00****00",
	"0******0",
	"0******0",
	"0*****00",
	"00000000"
]

def show_png(png):
	temp=list(png)
	b=png[0]
	letter=[[],[],[],[],[],[],[],[]]
	a=[]
	#print(temp)
	for i in range(8):
		for j in range(8):
			if temp[i][j]=="*":
				letter[i].append(j)
	print(letter)
	for k in range(100):
		for  i in range(8):
			line(i+1,letter[i])


while True:
	show_png(png1)
	if u1.value()==0:
		for k in range(30):
			show_png(png1)
		i=1
	if u2.value()==0:
		for k in range(30):
			show_png(png1)
		j=1
		if i==1:
			for k in range(30):
				show_png(png_0)
		elif i==2:
			for k in range(30):
				show_png(png_1)
		else:
			for k in range(30):
				show_png(png_2)

	show_png(png2)
	if u1.value()==0:
		for k in range(30):
			show_png(png2)
		i=2
	if u2.value()==0:
		for k in range(30):
			show_png(png2)
		j=2
		if i==1:
			for k in range(30):
				show_png(png_2)
		elif i==2:
			for k in range(30):
				show_png(png_0)
		else:
			for k in range(30):
				show_png(png_1)
	show_png(png3)
	if u1.value()==0:
		for k in range(30):
			show_png(png3)
		i=3
	if u2.value()==0:
		for k in range(30):
			show_png(png3)
		j=3
		if i==1:
			for k in range(30):
				show_png(png_1)
		elif i==2:
			for k in range(30):
				show_png(png_2)
		else:
			for k in range(30):
				show_png(png_0)
