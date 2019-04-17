from machine import Pin
import time
import text
import screen
import uturtle
turtle = uturtle.Turtle()

# 显示布局
screen_width = 240
screen_height = 320
margin = 5
button_width = (screen_width - margin*7) / 4
button_height = (screen_height - margin*8) / 5

# 按键
keys = [Pin(p,Pin.IN) for p in [35,36,39,34]]
keymatch = ["Key1","Key2","Key3","Key4"]
keyboard = [[1,2,3,123],[4,5,6,456],[7,8,9,789],[10,0,11,12]]
key_dict = {1:'1', 2:'2', 3:'3', 123:'+', 
			4:'4', 5:'5', 6:'6', 456:'-', 
			7:'7', 8:'8', 9:'9', 789:'×', 
			10:'.', 0:'0', 11:'=', 12:'÷'}

# 按键选择
select_xi = 0
select_yi = 0
keylist = []

l_operand = 0
r_operand = 0
operator = 123
dot_flag = 0
dot_loc = 0
result = 0

def calculate(l_operand, operator, r_operand):
	global key_dict
	if key_dict[operator] == '+':
		res = l_operand + r_operand
	elif key_dict[operator] == '-':
		res = l_operand - r_operand
	elif key_dict[operator] == '×':
		res = l_operand * r_operand
	elif key_dict[operator] == '÷':
		res = l_operand / r_operand
	else:
		res = r_operand
	return res

def get_results(num):
	global l_operand, operator, r_operand, keyboard, result, dot_flag, dot_loc
	if num < 10:
		if operator == 11:
			r_operand = 0
		if dot_flag == 0:
			r_operand = r_operand * 10 + num
		else:
			dot_loc = dot_loc + dot_flag
			r_operand = r_operand + num / (10 ** dot_loc)
		result = r_operand
	elif num == 10:
		if dot_flag == 0:
			dot_flag = 1
	elif num == 11:
		dot_flag = 0
		dot_loc = 0
		r_operand = calculate(l_operand, operator, r_operand)
		l_operand = 0
		operator = num
		result = r_operand
	elif num > 11:
		dot_flag = 0
		dot_loc = 0
		l_operand = calculate(l_operand, operator, r_operand)
		r_operand = 0
		operator = num
		result = l_operand
	else:
		print('input error')
	return str(l_operand)


# 画矩形
def draw_rect(x1, y1, x2, y2, lineWidth, lineColor):
	x = int(x1)
	y = int(y1)
	w = int(x2 - x1)
	h = int(y2 - y1)
	screen.drawline(x    , y    , x + w, y    , lineWidth, lineColor)
	screen.drawline(x + w, y    , x + w, y + h, lineWidth, lineColor)
	screen.drawline(x + w, y + h, x    , y + h, lineWidth, lineColor)
	screen.drawline(x    , y + h, x    , y    , lineWidth, lineColor)

# 画界面框架
def draw_interface():
	# 显示框
	x1 = margin * 2
	y1 = margin * 2
	x2 = screen_width - margin * 2
	y2 = margin * 2 + button_height
	draw_rect(x1, y1, x2, y2, 2, 0x00ffff)
	
	# 16个按键
	x = margin * 2
	y = margin * 2 + button_height + margin
	for i in range(4):
		draw_y = y + i * (button_height + margin)
		for j in range(4):
			draw_x = x + j * (button_width + margin)
			draw_rect(draw_x, draw_y, draw_x + button_width, draw_y + button_height, 2, 0x00ff00)

# 显示按键文字
def show_keyboard():
	global keyboard, key_dict
	for i in range(4):
		for j in range(4):
			num = keyboard[j][i]
			select_x = i * (button_width + margin) + 28
			select_y = (j + 1) * (button_height + margin) + 30
			text.draw(key_dict[num], int(select_x), int(select_y), 0x000000, 0xffffff)

# 按键选择初始化
def select_init():
	global select_xi, select_yi, keylist, l_operand, r_operand, operator, result, dot_flag, dot_loc
	select_xi = 0
	select_yi = 0
	keylist = []
	
	l_operand = 0
	r_operand = 0
	operator = 123
	dot_flag = 0
	dot_loc = 0
	result = 0
	
	select_x = margin*3
	select_y = button_height - margin*3
	text.draw('            0', int(select_x), int(select_y), 0x000000, 0xffffff)
	
	num = keyboard[select_yi][select_xi]
	select_x = margin * 2
	select_y = margin * 2 + button_height + margin
	draw_rect(select_x, select_y, select_x + button_width, select_y + button_height, 2, 0xff0000)

# 按键函数
def pressKeyboardEvent(key):
	global keymatch, keyboard, key_dict, select_xi, select_yi, keylist, result
	
	# 横行移动键
	if keymatch[key] == "Key1":
		num = keyboard[select_yi][select_xi]
		select_x = select_xi * (button_width + margin) + margin * 2
		select_y = select_yi * (button_height + margin) + margin * 2 + button_height + margin
		draw_rect(select_x, select_y, select_x + button_width, select_y + button_height, 2, 0x00ff00)
		
		select_xi = (select_xi + 1) % 4
		num = keyboard[select_yi][select_xi]
		select_x = select_xi * (button_width + margin) + margin * 2
		draw_rect(select_x, select_y, select_x + button_width, select_y + button_height, 2, 0xff0000)
	
	# 纵向移动键
	elif keymatch[key] == "Key2":
		num = keyboard[select_yi][select_xi]
		select_x = select_xi * (button_width + margin) + margin * 2
		select_y = select_yi * (button_height + margin) + margin * 2 + button_height + margin
		draw_rect(select_x, select_y, select_x + button_width, select_y + button_height, 2, 0x00ff00)
		
		select_yi = (select_yi + 1) % 4
		num = keyboard[select_yi][select_xi]
		select_y = select_yi * (button_height + margin) + margin * 2 + button_height + margin
		draw_rect(select_x, select_y, select_x + button_width, select_y + button_height, 2, 0xff0000)
	
	# 确认键
	elif keymatch[key] == "Key3":
		num = keyboard[select_yi][select_xi]
		get_results(num)
		select_x = margin*3
		select_y = button_height - margin*3
		text.draw('            ', int(select_x), int(select_y), 0x000000, 0xffffff)
		
		results = str(result)
		length = len(results)
		if length >= 13:
			length = 13
		select_x = int(screen_width - margin*3 - 16 * length)
		select_y = int(button_height - margin*3)
		text.draw(results[0:13], int(select_x), int(select_y), 0x000000, 0xffffff)
	
	# 清空键
	else:
		num = keyboard[select_yi][select_xi]
		select_x = select_xi * (button_width + margin) + margin * 2
		select_y = select_yi * (button_height + margin) + margin * 2 + button_height + margin
		draw_rect(select_x, select_y, select_x + button_width, select_y + button_height, 2, 0x00ff00)
		
		select_init()

# 初始化
screen.clear()
draw_interface()
show_keyboard()
select_init()

while True:
	i = 0
	j = -1
	for k in keys:
		if(k.value() == 0):
			if i!=j:
				j = i
				pressKeyboardEvent(i)
		i = i+1
		if(i > 3):
			i = 0
	time.sleep_ms(100)

