from machine import Pin
import time
import screen
import text


class calculator():
    def __init__(self):
        # 布局变量
        self.screen_width = 240
        self.screen_height = 320
        self.margin = 5
        self.button_width = (self.screen_width - self.margin * 7) / 4
        self.button_height = (self.screen_height - self.margin * 8) / 5

        # 按键变量
        self.keys = [Pin(p, Pin.IN) for p in [35, 36, 39, 34]]
        self.keymatch = ["Key1", "Key2", "Key3", "Key4"]
        self.keyboard = [[1, 2, 3, 123],
                         [4, 5, 6, 456],
                         [7, 8, 9, 789],
                         [10, 0, 11, 12]]
        self.keydict = {1: '1', 2: '2', 3: '3', 123: '+',
                        4: '4', 5: '5', 6: '6', 456: '-',
                        7: '7', 8: '8', 9: '9', 789: '×',
                        10: '.', 0: '0', 11: '=', 12: '÷'}
        self.startX = self.margin * 2
        self.startY = self.margin * 2 + self.button_height + self.margin
        self.selectXi = 0
        self.selectYi = 0

        # 计算器变量
        self.l_operand = 0
        self.r_operand = 0
        self.operator = 123
        self.result = 0
        self.dotFlag = 0
        self.dotLoc = 0

        # 初始化界面
        self.displayInit()

    # 画矩形
    def drawRect(self, x1, y1, x2, y2, lineWidth, lineColor):
        x = int(x1)
        y = int(y1)
        w = int(x2 - x1)
        h = int(y2 - y1)
        screen.drawline(x, y, x + w, y, lineWidth, lineColor)
        screen.drawline(x + w, y, x + w, y + h, lineWidth, lineColor)
        screen.drawline(x + w, y + h, x, y + h, lineWidth, lineColor)
        screen.drawline(x, y + h, x, y, lineWidth, lineColor)

    # 画界面
    def drawInterface(self):
        # 显示框
        x1 = self.margin * 2
        y1 = self.margin * 2
        x2 = self.screen_width - self.margin * 2
        y2 = self.margin * 2 + self.button_height
        self.drawRect(x1, y1, x2, y2, 2, 0x00ffff)
        # 16个按键
        for i in range(4):
            y = self.startY + i * (self.button_height + self.margin)
            for j in range(4):
                x = self.startX + j * (self.button_width + self.margin)
                self.drawRect(x, y, x + self.button_width, y + self.button_height, 2, 0x00ff00)

    # 显示按键文字
    def showKeyboard(self):
        for i in range(4):
            for j in range(4):
                num = self.keyboard[j][i]
                x = i * (self.button_width + self.margin) + 28
                y = (j + 1) * (self.button_height + self.margin) + 30
                text.draw(self.keydict[num], int(x), int(y), 0x000000, 0xffffff)

    # 按键选择初始化
    def selectInit(self):
        # 变量初始化
        self.selectXi = 0
        self.selectYi = 0

        self.l_operand = 0
        self.r_operand = 0
        self.operator = 123
        self.result = 0
        self.dotFlag = 0
        self.dotLoc = 0

        # 显示初始化
        x = self.margin * 3
        y = self.button_height - self.margin * 3
        text.draw('            0', int(x), int(y), 0x000000, 0xffffff)

        # 选择初始化
        x = self.startX
        y = self.startY
        self.drawRect(x, y, x + self.button_width, y + self.button_height, 2, 0xff0000)

    # 界面初始化
    def displayInit(self):
        screen.clear()
        self.drawInterface()
        self.showKeyboard()
        self.selectInit()

    # 计算器四则运算
    def calculate(self, op1, ope, op2):
        if self.keydict[ope] == '+':
            res = op1 + op2
        elif self.keydict[ope] == '-':
            res = op1 - op2
        elif self.keydict[ope] == '×':
            res = op1 * op2
        elif self.keydict[ope] == '÷':
            res = op1 / op2
        else:
            res = op2
        return res

    # 计算器算法
    def sendData(self, num):
        # 数字0-9
        if num < 10:
            if self.operator == 11:
                self.r_operand = 0
                self.operator = 123
            if self.dotFlag == 0:
                self.r_operand = self.r_operand * 10 + num
            else:
                self.dotLoc = self.dotLoc + self.dotFlag
                self.r_operand = self.r_operand + num / (10 ** self.dotLoc)
            self.result = self.r_operand
        # 小数点.
        elif num == 10:
            if self.dotFlag == 0:
                self.dotFlag = 1
        # 等号=
        elif num == 11:
            self.dotFlag = 0
            self.dotLoc = 0
            self.r_operand = self.calculate(self.l_operand, self.operator, self.r_operand)
            self.l_operand = 0
            self.operator = num
            self.result = self.r_operand
        # 运算符+-*/
        elif num > 11:
            self.dotFlag = 0
            self.dotLoc = 0
            self.l_operand = self.calculate(self.l_operand, self.operator, self.r_operand)
            self.r_operand = 0
            self.operator = num
            self.result = self.l_operand
        else:
            print('input error')

    # 按键事件处理
    def keyboardEvent(self, key):
        # 右移选择键
        if self.keymatch[key] == "Key1":
            # 取消前一个选择
            num = self.keyboard[self.selectYi][self.selectXi]
            x = self.selectXi * (self.button_width + self.margin) + self.startX
            y = self.selectYi * (self.button_height + self.margin) + self.startY
            self.drawRect(x, y, x + self.button_width, y + self.button_height, 2, 0x00ff00)
            # 选择右边一个
            self.selectXi = (self.selectXi + 1) % 4
            num = self.keyboard[self.selectYi][self.selectXi]
            x = self.selectXi * (self.button_width + self.margin) + self.startX
            self.drawRect(x, y, x + self.button_width, y + self.button_height, 2, 0xff0000)

        # 纵向移动键
        elif self.keymatch[key] == "Key2":
            # 取消前一个选择
            num = self.keyboard[self.selectYi][self.selectXi]
            x = self.selectXi * (self.button_width + self.margin) + self.startX
            y = self.selectYi * (self.button_height + self.margin) + self.startY
            self.drawRect(x, y, x + self.button_width, y + self.button_height, 2, 0x00ff00)
            # 选择右边一个
            self.selectYi = (self.selectYi + 1) % 4
            num = self.keyboard[self.selectYi][self.selectXi]
            y = self.selectYi * (self.button_height + self.margin) + self.startY
            self.drawRect(x, y, x + self.button_width, y + self.button_height, 2, 0xff0000)

        # 确认键
        elif self.keymatch[key] == "Key3":
            num = self.keyboard[self.selectYi][self.selectXi]
            self.sendData(num)
            # 清空显示区
            x = self.margin * 3
            y = self.button_height - self.margin * 3
            text.draw('            ', int(x), int(y), 0x000000, 0xffffff)
            # 显示结果
            results = str(self.result)
            length = len(results)
            if length >= 13:
                length = 13
            x = self.screen_width - self.margin * 3 - 16 * length
            y = self.button_height - self.margin * 3
            text.draw(results[0:13], int(x), int(y), 0x000000, 0xffffff)

        # 清空键
        else:
            # 取消前一个选择
            num = self.keyboard[self.selectYi][self.selectXi]
            x = self.selectXi * (self.button_width + self.margin) + self.startX
            y = self.selectYi * (self.button_height + self.margin) + self.startY
            self.drawRect(x, y, x + self.button_width, y + self.button_height, 2, 0x00ff00)
            # 按键选择初始化
            self.selectInit()

    # 开始运行
    def start(self):
        while True:
            i = 0
            j = -1
            for k in self.keys:
                if (k.value() == 0):
                    if i != j:
                        j = i
                        self.keyboardEvent(i)
                i = i + 1
                if (i > 3):
                    i = 0
            time.sleep_ms(130)  # 按键去抖


if __name__ == '__main__':
    ca = calculator()
    ca.start()
