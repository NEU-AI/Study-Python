from machine import Pin
import time
from random import randint
import screen
import text

pins = [36,39,34,35]
keys = []
brick = [
	[
		[
			[1,1,1],
			[0,0,1],
			[0,0,0]
		],
		[
			[0,0,1],
			[0,0,1],
			[0,1,1]
		],
		[
			[0,0,0],
			[1,0,0],
			[1,1,1]
		],
		[
			[1,1,0],
			[1,0,0],
			[1,0,0]
		]
	],
	[
		[
			[0,0,0],
			[0,1,1],
			[0,1,1]
		],
		[
			[0,0,0],
			[0,1,1],
			[0,1,1]
		],
		[
			[0,0,0],
			[0,1,1],
			[0,1,1]
		],
		[
			[0,0,0],
			[0,1,1],
			[0,1,1]
		]
	],
	[
		[
			[1,1,1],
			[0,1,0],
			[0,1,0]
		],
		[
			[0,0,1],
			[1,1,1],
			[0,0,1]
		],
		[
			[0,1,0],
			[0,1,0],
			[1,1,1]
		],
		[
			[1,0,0],
			[1,1,1],
			[1,0,0]
		]
	],
	[
		[
			[0,1,0],
			[0,1,0],
			[0,1,0]
		],
		[
			[0,0,0],
			[1,1,1],
			[0,0,0]
		],
		[
			[0,1,0],
			[0,1,0],
			[0,1,0]
		],
		[
			[0,0,0],
			[1,1,1],
			[0,0,0]
		]
	]
]

for p in pins:
	keys.append(Pin(p,Pin.IN))

class Grid(object):
	def __init__(self, master = None, x = 10, y = 10, w = 193, h = 303):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.rows = h//10
		self.cols = w//10
		self.bg = 0x000000;
		print(self.rows,self.cols)
		
		#画背景
		for i in range(320):
			screen.drawline(0, i, 239, i, 1, self.bg);
		
		#画边界
		screen.drawline(x,			y,		x + w - 1,	y,		1,	0xFFFFFF);
		screen.drawline(x + w - 1,	y,		x + w - 1,	y + h,	1,	0xFFFFFF);
		screen.drawline(x,			y + h,	x + w - 1,	y + h,	1,	0xFFFFFF);
		screen.drawline(x,			y,		x,			y + h,	1,	0xFFFFFF);

		#画提示框边界
		screen.drawline(204,			10,			204 + 32 - 1,	10,			1,	0xFFFFFF);
		screen.drawline(204 + 32 - 1,	10,			204 + 32 - 1,	10 + 32,	1,	0xFFFFFF);
		screen.drawline(204,			10 + 32,	204 + 32 - 1,	10 + 32,	1,	0xFFFFFF);
		screen.drawline(204,			10,			204,			10 + 32,	1,	0xFFFFFF);
	
	def drawgrid(self, pos, color):
		x = pos[1] * 10 + self.x + 2
		y = pos[0] * 10 + self.y + 2
		for i in range(9):
			screen.drawline(x, y + i, x + 9 - 1, y + i, 1, color);
	
	def drawpre(self, pos, color):
		x = pos[1] * 10 + 204 + 2
		y = pos[0] * 10 + 10  + 2
		for i in range(9):
			screen.drawline(x, y + i, x + 9 - 1, y + i, 1, color);
	

class Game(Grid):
	def __init__(self):
		super().__init__()
		self.back = [[0 for i in range(0, self.cols)] for i in range(0, self.rows)]
		self.matrix_o = [[0 for i in range(0, self.cols)] for i in range(0, self.rows)]
		self.curRow = -10
		self.curCol = -10
		self.start  = True
		self.shape  = -1
		self.isDown = True
		self.oldrow = 0
		self.oldcol = 0
		#当前有方块的开始行
		self.haverow = 29
		self.nextBrick = -1
		self.shape = 0 
		self.arr = [[0 for i in range(0,3)] for i in range(0,3)]
		self.nextarr = [[0 for i in range(0,3)] for i in range(0,3)]
		#使用一个字典将数字与其对应的颜色存放起来
		self.color = { 0:0x0000FF, 1:0x00FF00, 2:0xFF0000, 3:0xFFFF00 }
	def drawBack(self, rownum):
		for i in range(self.haverow, rownum + 1):
			for j in range(0, self.cols):
				pos = (i, j)
				if self.back[i][j] == 0:
					self.drawgrid(pos, self.bg)
				else:
					self.drawgrid(pos, 0x00FFFF)
		self.haverow += 1
		if self.haverow >= self.rows:
			self.haverow = self.rows - 1
	def drawRect(self):
		for i in range(0, len(self.nextarr)):
			for j in range(0, len(self.nextarr[i])):
				pos = (i, j)
				if self.nextarr[i][j] == 0:
					self.drawpre(pos, self.bg);
				elif self.nextarr[i][j] == 1:
					self.drawpre(pos, self.color[self.nextBrick])
		#print(self.oldrow, self.oldcol)
		#print(self.isDown)
		for i in range(0, 3):
			for j in range(0, 3):
				print("oldrow+i=", self.oldrow + i, self.oldcol + j) 
				if ((self.oldrow + i) >= self.rows) or ((self.oldcol + j) >= self.cols) or ((self.oldcol + j) < -1):
					break
				if self.oldcol+j < 0:
					pos = (self.oldrow + i, 0)
				else:
					pos = (self.oldrow + i, self.oldcol + j)
				if self.back[self.oldrow + i][self.oldcol + j] == 0:
					self.drawgrid(pos, self.bg);
		#绘制当前正在运动的方块
		#print(self.curRow,self.curCol)
		if (self.curRow != -10) and (self.curCol != -10):
			for i in range(0, len(self.arr)):
				for j in range(0, len(self.arr[i])):
					if self.arr[i][j] == 1:
						pos = (self.curRow + i,self.curCol + j)
						if self.isDown:
							if i < self.haverow:
								self.haverow = i
							self.drawgrid(pos, 0x00FFFF)
						else:
							self.drawgrid(pos, self.color[self.curBrick])
		#判断方块是否已经运动到达底部
		if self.isDown:
			for i in range(0, 3):
				for j in range(0, 3):
					if self.arr[i][j] != 0:
						self.back[self.curRow + i][self.curCol + j] = self.arr[i][j]
			self.oldrow = 0
			self.oldcol = 0
			#判断整行消除
			self.removeRow() 

			self.isDead()
			#获得下一个方块
			self.getCurBrick()
		else:
			self.oldrow = self.curRow
			self.oldcol = self.curCol
	#判断是否有整行需要消除
	def removeRow(self):
		rownum = 0
		print("removeRow")  
		for i in range(0, self.rows):
			tag1 = True
			for j in range(0, self.cols):
				if self.back[i][j]==0:
					tag1 = False
					break
			if tag1 == True:
				print(i, j)
				rownum = i
				#从上向下挪动
				for m in range(i-1, 0, -1):
					for n in range(0,self.cols):
						self.back[m + 1][n] = self.back[m][n]
		print(rownum)
		if rownum > 0:
			self.drawBack(rownum)
	#获得当前的方块
	def getCurBrick(self):
		self.shape = 0
		if self.nextBrick == -1: 
			self.curBrick = randint(0, len(brick)-1) 
			self.nextBrick = randint(0, len(brick)-1)
		elif self.isDown:
			self.curBrick = self.nextBrick
			self.nextBrick = randint(0, len(brick)-1)
		self.nextarr = brick[self.nextBrick][self.shape] 
		#self.curBrick = 3
		#当前方块数组
		self.arr = brick[self.curBrick][self.shape]
		#self.nextarr = self.arr
		self.curRow = -1
		self.curCol = 8
		#是否到底部为False
		self.isDown = False
	def onKeyboardEvent(self, key):
		keymatch=["Down", "Left", "Up", "Right"]
		#未开始，不必监听键盘输入
		if self.start == False:
			return
		#记录原来的值
		tempCurCol = self.curCol
		tempCurRow = self.curRow
		tempShape = self.shape
		tempArr = self.arr
		direction = -1
		print(keymatch[key])
		if keymatch[key] == "Left":
			#左移
			self.curCol -= 1
			direction = 1
		elif keymatch[key] == "Up":
		#变化方块的形状
			self.shape += 1
			direction = 2
			if self.shape >= 4:
				self.shape = 0
			self.arr = brick[self.curBrick][self.shape]
		elif keymatch[key] == "Right":
			direction = 3
			#右移
			self.curCol += 1
		elif keymatch[key] == "Down":
			direction = 4
			#下移
			self.curRow += 2
		if self.isEdge(direction) == False:
			self.curCol = tempCurCol
			self.curRow = tempCurRow
			self.shape = tempShape
			self.arr = tempArr
		#self.drawRect()
		return True

	#判断当前方块是否到达边界
	def isEdge(self, direction):
		tag = True 
		#print(direction)
		#向左，判断边界
		if direction == 1:
			for i in range(0, 3):
				for j in range(0, 3):
					if (self.arr[j][i] != 0) and (self.curCol + i < 0 or self.back[self.curRow + j][self.curCol + i] != 0):
						tag = False
						break 
		#向右，判断边界
		elif direction == 3:
			for i in range(0, 3):
				for j in range(0, 3):
					if (self.arr[j][i] != 0) and (self.curCol + i >= self.cols or self.back[self.curRow + j][self.curCol + i] != 0):
						tag = False
						break
		#向下，判断底部
		elif direction == 4:
			for i in range(0, 3):
				for j in range(0, 3):
					if (self.arr[i][j] != 0) and (self.curRow + i >= self.rows or self.back[self.curRow + i][self.curCol + j] != 0):
						tag = False
						self.isDown = True
						break
		#进行变形，判断边界
		elif direction == 2:
			if self.curCol < 0:
				self.curCol = 0
			if self.curCol + 2 >= self.cols:
				self.curCol = self.cols - 3
			if self.curRow + 2 >= self.rows:
				self.curRow = self.curRow - 3
		return tag
		
	def isDead(self):
		for j in range(0,len(self.back[0])):
			if self.back[0][j]!=0:
				print("GAME OVER")
				text.draw("GAME OVER", 34, 150, 0xFF0000, 0x000000)
				self.start = False;
				break;

	#方块向开始下移动  
	def brickStart(self):
		while True:
			#需要进行垃圾回收
			gc.collect()
			
			if self.start == False:
				print("exit thread")
				break
			if self.isDown:
				self.getCurBrick()
			i = 0
			j = -1
			for k in keys:
				if k.value() == 0:
					if i != j:
						print("i=", i)
						print("j=", j)
						j = i
						self.onKeyboardEvent(i)
				i = i + 1
				if i > 3:
					i = 0
			
			tempRow = self.curRow;
			self.curRow += 1
			if self.isEdge(4) == False:
				self.curRow = tempRow 
			#每一秒下降一格
			time.sleep_ms(120)
			self.drawRect()
			
		
if __name__ == '__main__':
	game = Game()
	game.brickStart()
