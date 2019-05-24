#---------- 配置信息 ----------
PASSWORD = "2354352";					#【密码】支持1-15位密码，密码内容支持 "2"、"3"、"4"、"5"
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
import text;

PASSWORD_CHARS = ["2", "3", "4", "5"];
PASSWORD_MASK = "*";

SW = 240;
SH = 320;
CW = 16;
CH = 16;

OUTPUT_OPEN = 0;
OUTPUT_CLOSE = 1;

OUTPUT = machine.Pin(21, machine.Pin.OUT);
OUTPUT.value(OUTPUT_CLOSE);
PADS = [machine.TouchPad(machine.Pin(i)) for i in [4, 32, 33, 27]];
KEYS = [machine.Pin(i, machine.Pin.IN) for i in [36,39,34,35]];
KEY_EVENT_HANDLER = [];

password_len = len(PASSWORD);
password_posX_array = [];

password_input_array = [];

key_last_state = [];		#PADS, KEYS
key_new_state = [];

password_show = False;
flag_error = False;

def text_with_shadow(msg, x = False, y = False, fgColor = 0x000000, bgColor = 0xEEEEEE, shadowBgColor = 0xCCCCCC, shadowOffsetX = 0, shadowOffsetY = 2):
	msg_len = len(msg);
	
	if x is False:
		x = (SW - CW * msg_len) // 2;
	if y is False:
		y = (SH - CH) // 2;
	
	if shadowBgColor is not False:
		text.draw("　" * msg_len, x + shadowOffsetX, y + shadowOffsetY, fgColor, shadowBgColor);
	
	if bgColor is False:
		text.draw(msg, x, y, fgColor);
	else:
		text.draw(msg, x, y, fgColor, bgColor);
	

def text_error(err_msg):
	global flag_error;
	
	screen.clear();
	text_with_shadow("系统内部错误：" + err_msg);
	flag_error = True;
	

def text_password(index, password_mask = True):
	if (index < 0) or (index >= password_len) or (password_mask and (index >= len(password_input_array))):
		text_error("密码索引错误");
	else:
		if password_mask:
			if password_show:
				text_with_shadow(password_input_array[index], x = password_posX_array[index], fgColor = 0x222222);
			else:
				text_with_shadow(PASSWORD_MASK, x = password_posX_array[index], fgColor = 0x222222);
		else:
			text_with_shadow("　", x = password_posX_array[index], fgColor = 0x222222);
	

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
	
	text_with_shadow("请输入解锁密码：", y = 67, shadowOffsetX = 2);
	if PASSWORD_SHOW_ENABLE:
		text_with_shadow("【S1】显示密码", y = 212, shadowOffsetX = 2);
		text_with_shadow("【S2】清空密码", y = 236, shadowOffsetX = 2);
		text_with_shadow("【S4】删除密码", y = 260, shadowOffsetX = 2);
	else:
		text_with_shadow("【S2】清空密码", y = 224, shadowOffsetX = 2);
		text_with_shadow("【S4】删除密码", y = 248, shadowOffsetX = 2);

	for i in range(password_len):
		text_password(i, False);
	

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
		text_with_shadow("解锁成功！%d秒后返回..." % WAIT_S_SUCCESS, shadowOffsetX = 2);
		time.sleep_ms(1000);
		for i in range(WAIT_S_SUCCESS - 1):
			text_with_shadow("解锁成功！%d秒后返回..." % (WAIT_S_SUCCESS - i - 1), shadowBgColor = False);
			time.sleep_ms(1000);
		
		lock_close();
		
		initialize();
	else:
		print("解锁失败！");
		
		screen.clear();
		text_with_shadow("解锁失败！%d秒后返回..." % WAIT_S_FAIL, shadowOffsetX = 2);
		time.sleep_ms(1000);
		for i in range(WAIT_S_FAIL - 1):
			text_with_shadow("解锁失败！%d秒后返回..." % (WAIT_S_FAIL - i - 1), shadowBgColor = False);
			time.sleep_ms(1000);
		
		initialize();
	

def handle_password_push(password_char):
	if len(password_input_array) >= password_len:
		text_error("密码溢出");
	else:
		password_input_array.append(password_char);
		text_password(len(password_input_array) - 1);
		if len(password_input_array) == password_len:
			handle_password_finish();
			return True;
		
	return False;
	

def handle_password_pop():
	if len(password_input_array) == 0:
		text_error("密码索引错误");
	else:
		password_input_array.pop();
		text_password(len(password_input_array), False);
	

def initialize_pos():
	#计算密码显示横坐标
	space_password = (SW - CW * password_len) // (password_len + 1);
	space_left = (SW - CW * password_len - space_password * (password_len - 1)) // 2;
	for i in range(password_len):
		x = space_left + (CW + space_password) * i;
		password_posX_array.append(x);
	

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
					text_password(i, True);
				text_with_shadow("【S1】隐藏密码" if password_show else "【S1】显示密码", y = 212, shadowBgColor = False);
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
if (password_len < 1) or (password_len > 15):
	text_with_shadow("只支持1-15位密码长度！", shadowOffsetX = 2);
elif (WAIT_S_SUCCESS >= 10) or (WAIT_S_FAIL >= 10):
	text_with_shadow("延时需小于10秒！", shadowOffsetX = 2);
else:
	#验证密码内容
	password_valid = True;
	for i in range(password_len):
		if PASSWORD[i] not in PASSWORD_CHARS:
			password_valid = False;
			break;
	if not password_valid:
		text_with_shadow("密码中含有不符合规范的字符！", shadowOffsetX = 2);
	else:
		initialize_pos();
		initialize_key_handle();
		initialize();
		handle_keyEvent();
		print("程序退出了！");
	
