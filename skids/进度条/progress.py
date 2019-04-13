import uturtle
from machine import Timer
import text
import screen
turtle = uturtle.Turtle()
class prog():
	def __init__(self):
		screen.clear()
	def rect1(self,x, y, color, x2, y2):
		width = abs(x2 - x)
		height = abs(y2 - y)
		turtle.pencolor(color)
		turtle.penup()
		turtle.goto(x,y)
		turtle.pendown()
		turtle.setheading(0)
		turtle.fd(width)
		turtle.right(90)
		turtle.forward(height)
		turtle.right(90)
		turtle.forward(width)
		turtle.right(90)
		turtle.forward(height)
	def rect2(self,x, y, color, x2, y2):
		width = abs(x2 - x)
		height = abs(y2 - y)
		turtle.pencolor(color)
		turtle.penup()
		turtle.goto(x,y)
		turtle.pendown()
		turtle.setheading(0)
		turtle.fillcolor(color)
		turtle.begin_fill()
		turtle.fd(width)
		turtle.right(90)
		turtle.forward(height)
		turtle.right(90)
		turtle.forward(width)
		turtle.right(90)
		turtle.forward(height)
		turtle.end_fill()
		
	def progress(self):
		self.rect1(-50,50,'black',50,30)
		x0=-50
		y0=50
		timer= Timer(-1)
		for i in range(1,26):
			timer.init(mode=Timer.ONE_SHOT, period=1000,callback=self.rect2(x0,y0,'black',x0+4,30))	
			x0+=4
		text.draw("加载完成",88,160,0xff0000)	
if __name__ == '__main__':
    pr = prog()
    pr.progress()
	