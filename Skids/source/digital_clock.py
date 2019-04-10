import time
import text
import screen


class DigitalClock():
    def __init__(self, hour, minute, second):
        # 布局变量
        self.startX = 10  # 时钟左上角坐标X
        self.startY = 100  # 时钟左上角坐标Y
        self.margin = 8  # 数字健距
        self.edgeL = 24  # 数字边长
        self.edgeW = 2  # 数字边宽
        self.colon = int(self.edgeL / 2)  # 冒号间距

        # 显示变量
        self.colorDict = {0: 0xffffff, 1: 0x000000}  # 数字边颜色0白色1黑色
        self.numDict = {0: (1, 0, 1, 1, 1, 1, 1),  # 数字对应的显示列表
                        1: (0, 0, 0, 0, 0, 1, 1),
                        2: (1, 1, 1, 0, 1, 1, 0),
                        3: (1, 1, 1, 0, 0, 1, 1),
                        4: (0, 1, 0, 1, 0, 1, 1),
                        5: (1, 1, 1, 1, 0, 0, 1),
                        6: (1, 1, 1, 1, 1, 0, 1),
                        7: (1, 0, 0, 0, 0, 1, 1),
                        8: (1, 1, 1, 1, 1, 1, 1),
                        9: (1, 1, 1, 1, 0, 1, 1)}

        # 时间变量
        self.hur = hour
        self.min = minute
        self.sec = second

        # 初始化显示
        screen.clear()
        self.displayColon()

    # 显示分隔符
    def displayColon(self):
        # 时分间
        x1 = self.startX + self.edgeL * 2 + self.margin + self.colon
        y1 = self.startY + self.margin
        x2 = x1
        y2 = y1 + self.margin
        screen.drawline(x1, y1, x2, y2, self.edgeW, 0x000000)
        y1 = self.startY + self.margin * 4
        y2 = y1 + self.margin
        screen.drawline(x1, y1, x2, y2, self.edgeW, 0x000000)

        # 分秒间
        x1 = self.startX + self.edgeL * 4 + self.margin * 2 + self.colon * 3
        y1 = self.startY + self.margin
        x2 = x1
        y2 = y1 + self.margin
        screen.drawline(x1, y1, x2, y2, self.edgeW, 0x000000)
        y1 = self.startY + self.margin * 4
        y2 = y1 + self.margin
        screen.drawline(x1, y1, x2, y2, self.edgeW, 0x000000)

    # 通过控制7条边的颜色显示出相应的数字
    def displayNum(self, num, x, y):  
        # 1号边
        x1 = x
        y1 = y
        x2 = x + self.edgeL
        y2 = y
        screen.drawline(x1, y1, x2, y2, self.edgeW, self.colorDict[num[0]])

        # 2号边
        x1 = x
        y1 = y + self.edgeL
        x2 = x + self.edgeL
        y2 = y + self.edgeL
        screen.drawline(x1, y1, x2, y2, self.edgeW, self.colorDict[num[1]])

        # 3号边
        x1 = x
        y1 = y + self.edgeL * 2
        x2 = x + self.edgeL
        y2 = y + self.edgeL * 2
        screen.drawline(x1, y1, x2, y2, self.edgeW, self.colorDict[num[2]])

        # 4号边
        x1 = x
        y1 = y
        x2 = x
        y2 = y + self.edgeL
        screen.drawline(x1, y1, x2, y2, self.edgeW, self.colorDict[num[3]])

        # 5号边
        x1 = x
        y1 = y + self.edgeL
        x2 = x
        y2 = y + self.edgeL * 2
        screen.drawline(x1, y1, x2, y2, self.edgeW, self.colorDict[num[4]])

        # 6号边
        x1 = x + self.edgeL
        y1 = y
        x2 = x + self.edgeL
        y2 = y + self.edgeL
        screen.drawline(x1, y1, x2, y2, self.edgeW, self.colorDict[num[5]])

        # 7号边
        x1 = x + self.edgeL
        y1 = y + self.edgeL
        x2 = x + self.edgeL
        y2 = y + self.edgeL * 2
        screen.drawline(x1, y1, x2, y2, self.edgeW, self.colorDict[num[6]])

    # 开始运行
    def start(self):
        while True:
            start = time.ticks_ms()  # 记录开始时间

            # 显示时
            hurH = int(self.hur / 10)
            hurL = self.hur % 10
            x = self.startX
            self.displayNum(self.numDict[hurH], x, self.startY)
            x = self.startX + self.edgeL + self.margin
            self.displayNum(self.numDict[hurL], x, self.startY)

            # 显示分
            minH = int(self.min / 10)
            minL = self.min % 10
            x = self.startX + self.edgeL * 2 + self.margin + self.colon * 2
            self.displayNum(self.numDict[minH], x, self.startY)
            x = self.startX + self.edgeL * 3 + self.margin * 2 + self.colon * 2
            self.displayNum(self.numDict[minL], x, self.startY)

            # 显示秒
            secH = int(self.sec / 10)
            secL = self.sec % 10
            x = self.startX + self.edgeL * 4 + self.margin * 2 + self.colon * 4
            self.displayNum(self.numDict[secH], x, self.startY)
            x = self.startX + self.edgeL * 5 + self.margin * 3 + self.colon * 4
            self.displayNum(self.numDict[secL], x, self.startY)

            # 计算下一时刻
            self.sec = self.sec + 1
            if self.sec >= 60:
                self.min = self.min + 1
                self.sec = 0
                if self.min >= 60:
                    self.hur = self.hur + 1
                    self.min = 0
                    if self.hur >= 24:
                        self.hur = 0

            # 一个循环执行1s
            time.sleep_ms(912)  # 程序执行时延大约88ms
            print(time.ticks_diff(time.ticks_ms(), start))  # 每一次循环运行时间


if __name__ == '__main__':
    dc = DigitalClock(23, 58, 30)  # 设置初始时间为23:58:30
    dc.start()

