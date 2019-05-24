#---------- 配置信息 ----------
PASSWORD = "2354352";					#【密码】支持1-10位密码，密码内容支持 "2"、"3"、"4"、"5"
PASSWORD_SHOW_ENABLE = True;			#【是否支持显示密码功能】为真值时支持显示密码功能
WAIT_S_SUCCESS = 5;						#【解锁成功时的等待时间】单位为秒，需要小于 10 秒
WAIT_S_FAIL = 1;						#【解锁失败时的等待时间】单位为秒，需要小于 10 秒
WAIT_MS_SCANKEY = 100;					#【扫描按钮状态的时间间隔】单位为毫秒，实际的时间间隔为 (WAIT_MS_SCANKEY + 按键处理函数的处理时间)
#------------------------------

#---------- 备注信息 ----------
#添加 gc 后，程序崩溃，原因未知
#------------------------------

import machine;
import screen;
import time;
import ubitmap;

PASSWORD_CHARS = ["2", "3", "4", "5"];
PASSWORD_MASK = "*";

OUTPUT_OPEN = 0;
OUTPUT_CLOSE = 1;

OUTPUT = machine.Pin(21, machine.Pin.OUT);
OUTPUT.value(OUTPUT_CLOSE);
PADS = [machine.TouchPad(machine.Pin(i)) for i in [4, 32, 33, 27]];
KEYS = [machine.Pin(i, machine.Pin.IN) for i in [36,39,34,35]];
KEY_EVENT_HANDLER = [];

password_len = len(PASSWORD);
password_posX = 70;
password_posY_array = [];

password_input_array = [];

key_last_state = [];		#PADS, KEYS
key_new_state = [];

password_show = False;
flag_error = False;

pic_tab = {
	'menu_S1_1' : ubitmap.BitmapFromFile("lock_pic/menu_S1_1"),
	'menu_S1_2' : ubitmap.BitmapFromFile("lock_pic/menu_S1_2"),
	'menu_S2'   : ubitmap.BitmapFromFile("lock_pic/menu_S2"),
	'menu_S4'   : ubitmap.BitmapFromFile("lock_pic/menu_S4"),
	
	'tip'			: ubitmap.BitmapFromFile("lock_pic/tip"),
	'tip_success'	: ubitmap.BitmapFromFile("lock_pic/tip_success"),
	'tip_failed'	: ubitmap.BitmapFromFile("lock_pic/tip_failed"),
	'tip_delay'	: ubitmap.BitmapFromFile("lock_pic/tip_delay"),
	
	'password' : {
		'blank' : ubitmap.BitmapFromFile("lock_pic/password/blank"),
		'mask'  : ubitmap.BitmapFromFile("lock_pic/password/mask"),
		'nums'  : [
			ubitmap.BitmapFromFile("lock_pic/password/num_0"),
			ubitmap.BitmapFromFile("lock_pic/password/num_1"),
			ubitmap.BitmapFromFile("lock_pic/password/num_2"),
			ubitmap.BitmapFromFile("lock_pic/password/num_3"),
			ubitmap.BitmapFromFile("lock_pic/password/num_4"),
			ubitmap.BitmapFromFile("lock_pic/password/num_5"),
			ubitmap.BitmapFromFile("lock_pic/password/num_6"),
			ubitmap.BitmapFromFile("lock_pic/password/num_7"),
			ubitmap.BitmapFromFile("lock_pic/password/num_8"),
			ubitmap.BitmapFromFile("lock_pic/password/num_9"),
		],
	},
	
	'splitter' : ubitmap.BitmapFromFile("lock_pic/splitter"),
};

def print_error(err_msg):
	global flag_error;
	
	screen.clear();
	print("系统内部错误：" + err_msg);
	flag_error = True;
	

def draw_password(index, password_mask = True):
	if (index < 0) or (index >= password_len) or (password_mask and (index >= len(password_input_array))):
		print_error("密码索引错误");
	else:
		if password_mask:
			if password_show:
				pic_tab["password"]["nums"][int(password_input_array[index])].draw(password_posX, password_posY_array[index]);
			else:
				pic_tab["password"]["mask"].draw(password_posX, password_posY_array[index]);
		else:
			pic_tab["password"]["blank"].draw(password_posX, password_posY_array[index]);
	

def initialize():
	global password_input_array;
	global key_last_state;
	global key_new_state;
	global password_show;
	
	#初始化界面
	screen.clear();
	
	password_show = False;
	
	for i in range(len(password_input_array)):
		password_input_array.pop();
	
	for i in range(len(key_last_state)):
		key_last_state.pop();
	for i in range(len(PADS)):
		key_last_state.append(False);
	for i in range(len(KEYS)):
		key_last_state.append(False);
	
	for i in range(len(key_new_state)):
		key_new_state.pop();
	
	if PASSWORD_SHOW_ENABLE:
		pic_tab["menu_S1_1"].draw(146, 9);
		pic_tab["menu_S2"].draw(111, 9);
		pic_tab["menu_S4"].draw(76, 9);
	else:
		pic_tab["menu_S2"].draw(130, 9);
		pic_tab["menu_S4"].draw(90, 9);
	
	pic_tab["splitter"].draw(0, 128);
	
	pic_tab["tip"].draw(165, 155);
	for i in range(password_len):
		draw_password(i, False);
	

def lock_open():
	print("lock_open");
	OUTPUT.value(OUTPUT_OPEN);

def lock_close():
	print("lock_close");
	OUTPUT.value(OUTPUT_CLOSE);

def handle_password_finish():
	if ("").join(password_input_array) == PASSWORD:
		print("解锁成功！");
		
		lock_open();
		
		screen.clear();
		pic_tab["tip_success"].draw(135, 115);
		pic_tab["tip_delay"].draw(87, 110);
		for i in range(WAIT_S_SUCCESS):
			pic_tab["password"]["nums"][WAIT_S_SUCCESS - i].draw(87, 112);
			time.sleep_ms(1000);
		
		lock_close();
		
		initialize();
	else:
		print("解锁失败！");
		
		screen.clear();
		pic_tab["tip_failed"].draw(135, 115);
		pic_tab["tip_delay"].draw(87, 110);
		for i in range(WAIT_S_FAIL):
			pic_tab["password"]["nums"][WAIT_S_FAIL - i].draw(87, 112);
			time.sleep_ms(1000);
		
		initialize();
	

def handle_password_push(password_char):
	if len(password_input_array) >= password_len:
		print_error("密码溢出");
	else:
		password_input_array.append(password_char);
		draw_password(len(password_input_array) - 1);
		if len(password_input_array) == password_len:
			handle_password_finish();
			return True;
		
	return False;
	

def handle_password_pop():
	if len(password_input_array) == 0:
		print_error("密码索引错误");
	else:
		password_input_array.pop();
		draw_password(len(password_input_array), False);
	

def initialize_pos():
	#计算密码显示横坐标
	space_password = (190 - 15 * password_len) // (password_len + 1);
	space_left = (190 - 15 * password_len - space_password * (password_len - 1)) // 2;
	for i in range(password_len):
		y = 130 + space_left + (15 + space_password) * i;
		password_posY_array.append(y);
	

def initialize_key_handle():
	def key_handler_SW2(down):
		if down == True:
			print("key_handler_SW2 DOWN");
			return handle_password_push("2");
		return False;
	
	def key_handler_SW3(down):
		if down == True:
			print("key_handler_SW3 DOWN");
			return handle_password_push("3");
		return False;
	
	def key_handler_SW4(down):
		if down == True:
			print("key_handler_SW4 DOWN");
			return handle_password_push("4");
		return False;
	
	def key_handler_SW5(down):
		if down == True:
			print("key_handler_SW5 DOWN");
			return handle_password_push("5");
		return False;
	
	def key_handler_S1(down):
		global password_show;
		
		if down == True:
			print("key_handler_S1 DOWN");
			password_show_new = PASSWORD_SHOW_ENABLE and (not password_show);
			if password_show_new != password_show:
				password_show = password_show_new;
				for i in range(len(password_input_array)):
					draw_password(i, True);
				if password_show:
					pic_tab["menu_S1_2"].draw(146, 9);
				else:
					pic_tab["menu_S1_1"].draw(146, 9);
		return False;
	
	def key_handler_S2(down):
		if down == True:
			print("key_handler_S2 DOWN");
			for i in range(len(password_input_array)):
				handle_password_pop();
		return False;
	
	def key_handler_S3(down):
		if down == True:
			print("key_handler_S3 DOWN");
		return False;
	
	def key_handler_S4(down):
		if down == True:
			print("key_handler_S4 DOWN");
			if len(password_input_array) > 0:
				handle_password_pop();
		return False;
	
	KEY_EVENT_HANDLER.append(key_handler_SW2);
	KEY_EVENT_HANDLER.append(key_handler_SW3);
	KEY_EVENT_HANDLER.append(key_handler_SW4);
	KEY_EVENT_HANDLER.append(key_handler_SW5);
	KEY_EVENT_HANDLER.append(key_handler_S1);
	KEY_EVENT_HANDLER.append(key_handler_S2);
	KEY_EVENT_HANDLER.append(key_handler_S3);
	KEY_EVENT_HANDLER.append(key_handler_S4);
	

def scan_key():
	global key_new_state;
	
	for i in range(len(key_new_state)):
		key_new_state.pop();
	
	for i in range(len(PADS)):
		key_new_state.append(PADS[i].read() <= 550);
	for i in range(len(KEYS)):
		key_new_state.append(KEYS[i].value() == 0);
	

def translate_key():
	global key_last_state;
	global key_new_state;
	
	for i in range(len(key_last_state)):
		if key_new_state[i] != key_last_state[i]:
			if KEY_EVENT_HANDLER[i](key_new_state[i]):
				break;
		

def handle_keyEvent():
	global flag_error;
	global key_last_state;
	global key_new_state;
	
	while not flag_error:
		scan_key();
		translate_key();
		
		key_last_state, key_new_state = key_new_state, key_last_state;
		
		#间隔时间应该是变化的
		time.sleep_ms(WAIT_MS_SCANKEY);
	

#验证密码长度
if (password_len < 1) or (password_len > 10):
	print_error("只支持1-10位密码长度！");
elif (WAIT_S_SUCCESS >= 10) or (WAIT_S_FAIL >= 10):
	print_error("延时需小于10秒！");
else:
	#验证密码内容
	password_valid = True;
	for i in range(password_len):
		if PASSWORD[i] not in PASSWORD_CHARS:
			password_valid = False;
			break;
	if not password_valid:
		print_error("密码中含有不符合规范的字符！");
	else:
		initialize_pos();
		initialize_key_handle();
		initialize();
		handle_keyEvent();
		print("程序退出了！");
	
