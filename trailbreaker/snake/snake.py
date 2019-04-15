import lcd_show
from lcd_show import *
from font import *
import pyb
from pyb import Pin
import time
import utime
from random import randint
import framebuf
#LCD
usrspi = USR_SPI(scl=Pin('X6',Pin.OUT_PP), sda=Pin('X7', Pin.OUT),dc=Pin('X8', Pin.OUT))
disp = DISPLAY(usrspi,cs=Pin('X5', Pin.OUT),res=Pin('X4', Pin.OUT),led_en=Pin('X3', Pin.OUT))
r=Pin('X9',Pin.OUT_PP)
r.low()
pins = ['Y7','Y8','Y5','Y6']
keys = []
for p in pins:
	keys.append(Pin(p,Pin.IN,Pin.PULL_UP))
class Grid(object):#网格类
	def __init__(self, master=None,x=8, y=8, w=12, h=12):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.width=w
		self.height=h
		self.bg=disp.WHITE
		disp.clr(disp.WHITE)

	def draw(self, pos, color):
		x = pos[0] * 8 + self.x+1
		y = pos[1] * 8 + self.y+1
		disp.putrect(x,y,8,8,color)

		
class Food(object):#食物类
	def __init__(self, grid, color = disp.GREEN):
		self.grid = grid
		self.color = color
		self.set_pos()
		self.type = 1
	def set_pos(self):#随机生成食物位置
		x = randint(0, 12)
		y = randint(0, 12)
		self.pos = (x, y)
	def display(self):#画点
		self.grid.draw(self.pos, self.color)
		
		
class Snake(object):#蛇类
	def __init__(self, grid, color = disp.BLUE):#初始化蛇身位置，方向，颜色
		self.grid = grid
		self.color = color
		self.body = [(5, 5), (5, 6), (5, 7)]
		self.direction = "Up"
		for i in self.body:
			self.grid.draw(i, self.color)
	def initial(self):#重新开始游戏时初始化蛇身位置，方向，颜色
		while not len(self.body) == 0:
			pop = self.body.pop()
			self.grid.draw(pop, disp.WHITE)
		self.body = [(8, 11), (8, 12), (8, 13)]
		self.direction = "Up"
		self.color = disp.BLUE
		for i in self.body:
			self.grid.draw(i, self.color)
	def move(self, new):#移动
		self.body.insert(0, new)
		pop = self.body.pop()
		self.grid.draw(pop, self.grid.bg)
		self.grid.draw(new, self.color)
	def add(self ,new):#长度增加
		self.body.insert(0, new)
		self.grid.draw(new, self.color)
		
 #蛇吃到了特殊食物1，剪短自身的长度
	def cut_down(self,new):
		self.body.insert(0, new)
		self.grid.draw(new, self.color)
		for i in range(0,3):
			pop = self.body.pop()
 			self.grid.draw(pop, self.grid.bg)

    #蛇吃到了特殊食物2，回到最初长度
	def init(self, new):
		self.body.insert(0, new)
		self.grid.draw(new, self.color)
		while len(self.body) > 3:
 			pop = self.body.pop()
			self.grid.draw(pop, self.grid.bg)

     #蛇吃到了特殊食物3，改变了自身的颜色,纯属好玩
	def change(self, new, color):
		self.color = color
		self.body.insert(0, new)
		for item in self.body:
			self.grid.draw(item, self.color)
class SnakeGame():	#游戏类
	def __init__(self):
		self.grid = Grid()
		print('1')
		self.snake = Snake(self.grid)
		print('2')
		self.food = Food(self.grid)
		print('3')
		self.gameover = False
		self.score = 0
		self.status = ['run', 'stop']
		self.speed = 300
		self.display_food()
		print('4')
	def display_food(self):#生成不同种食物
        	
		if randint(0, 40) == 5:
			self.food.color = disp.ORANGE
			self.food.type = 3
			while (self.food.pos in self.snake.body):
				self.food.set_pos()
			self.food.display()
		elif randint(0, 4) == 2:
			self.food.color = disp.PINK
			self.food.type = 4
			while (self.food.pos in self.snake.body):
				self.food.set_pos()
			self.food.display()
		elif len(self.snake.body) > 10 and randint(0, 16) == 5:
			self.food.color = disp.YELLOW
			self.food.type = 2
			while (self.food.pos in self.snake.body):
				self.food.set_pos()
			self.food.display()
		else:
			self.food.color = disp.GREEN
			self.food.type = 1
			while (self.food.pos in self.snake.body):
				self.food.set_pos()
			self.food.display()
		print(self.food.type)
	def initial(self):#游戏结束时，重新开始
		self.gameover = False
		self.score = 0
		self.snake.initial()
	def run(self):
		print('5')
		while True:
			i=0
			j=-1
			for k in keys:
				if k.value()==0:
					if i!=j:
						print("i=",i)
						print("j=",j)
						j=i
						self.key_release(i)
                
				i=i+1
				if i>3:
					i=0
          #首先判断游戏是否暂停
			if not self.status[0] == 'stop':
				if self.gameover == True:
					self.initial()
				else:
                #判断游戏是否结束
					self.move()
				time.sleep_ms(125)
	def move(self, color=disp.BLUE):
        # 计算蛇下一次移动的点
		head = self.snake.body[0]
        #print(self.snake.direction)
		if self.snake.direction == 'Up':
			if head[1] - 1 < 0:
				new = (head[0], 17)
			else:
				new = (head[0], head[1] - 1)
		elif self.snake.direction == 'Down':
			new = (head[0], (head[1] + 1) % 17)
		elif self.snake.direction == 'Left':
			if head[0] - 1 < 0:
				new = (13, head[1])
			else:
				new = (head[0] - 1, head[1])
		else:
			new = ((head[0] + 1) % 13, head[1])
            #撞到自己，设置游戏结束的标志位，等待下一循环
		if new in self.snake.body:
			self.gameover=True
        #吃到食物
		elif new == self.food.pos:
			print(self.food.type)
			if self.food.type == 1:
				self.snake.add(new)
				self.snake.change(new, disp.GREEN)

			elif self.food.type == 2:
				self.snake.cut_down(new)
				self.snake.change(new, disp.YELLOW)

			elif self.food.type == 4:
				self.snake.change(new, disp.PINK)
			else:

				self.snake.init(new)
				self.snake.change(new, disp.ORANGE)
			self.display_food()
		elif new == self.food.pos:
			self.snake.add(new)
			self.display_food()    
        #什么都没撞到，继续前进
		else:
			self.snake.move(new)

   




	def key_release(self, key):
        	keymatch=["Down","Left","Up","Right"]
        	key_dict = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        	print(keymatch[key])
        #蛇不可以像自己的反方向走
		if keymatch[key] in key_dict and not keymatch[key] == key_dict[self.snake.direction]:
			self.snake.direction = keymatch[key]
			self.move()

        
if __name__ == '__main__':
	snake = SnakeGame()
	snake.run()



















