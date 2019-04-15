from pyb import Pin

r=[Pin(i, Pin.OUT_PP) for i in ['X2','X1','X3','X4','X5','X6','X8','X7']]
for i in range (8):
	r[i].high()

c=[Pin(i, Pin.OUT_PP) for i in ['Y2','Y1','Y3','Y4','Y5','Y6','Y8','Y7']]
for i in range (8):
	c[i].high()

def line(row,colDisp):
	r[row-1].low() #打开某行
	for j in colDisp: 
		if (j>=0 and j<=7):
			c[j].low()#开启
			pyb.delay(1)
			c[j].high()#熄灭
	r[row-1].high()#关闭行

png=[
	"0*0000*0",
	"0*0**0*0",
	"0*0000*0",
	"0*0000*0",
	"0*0000*0",
	"0*0**0*0",
	"0*0000*0",
	"0*0000*0"
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




'''
		[#东
			[1,2,3,4,5,6,7, 8],
			[[3],
			[0,1,2,3,4,5,6],
			[1,3],
			[0,1,2,3,4,5,6],
			[3],
			[1,3,5],
			[0,2,3,6],
			[]]
		],
		[#北
			[1,2,3,4,5,6,7,8],
			[[2,4],
			[0,1,2,4,6],
			[2,4,5],
			[2,4],
			[2,4],
			[0,1,2,4,5,6],
			[2,4,7],
			[2,4,5,6,7]]
		],
		[#大
			[1,2,3,4,5,6,7,8],
			[
			[3],
			[3],
			[0,1,2,3,4,5,6],
			[3],
			[2,4],
			[1,5],
			[0,6],
			[]
			]
		],
		[#学
			[1,2,3,4,5,6,7,8],
			[[0,3,6],
			[0,1,2,3,4,5,6,7],
			[0,7],
			[2,3,4,5,7],
			[4],
			[1,2,3,4,5,6],
			[4],
			[3,4]]
		]'''
		
	





while True:
	show_png(png)
