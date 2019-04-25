from machine import Timer
import text
import screen
import time
class prog():
	def __init__(self):
		screen.clear()
		self.x=61
		self.quit_flag = False
		self.timer= Timer(-1)
		screen.drawline(60, 100, 180, 100, 1, 0x000000)
		screen.drawline(60, 130, 180, 130, 1, 0x000000)
		screen.drawline(60, 100, 60, 130, 1, 0x000000)
		screen.drawline(180, 100, 180, 130, 1, 0x000000)
	def rect(self,z):
		screen.drawline(self.x, 100, self.x, 130, 1, 0x000000)
		self.x+=1
		if self.x==180:
			self.timer.deinit()
			text.draw("加载完成",88,160,0xff0000)
			self.quit_flag = True;
	def progress(self):
		self.timer.init(mode=Timer.PERIODIC, period=1000,callback=self.rect)
		while not self.quit_flag:
			time.sleep_ms(50)
if __name__ == '__main__':
    pr = prog()
    pr.progress()
	