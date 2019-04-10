import math
import time
import screen


class AnalogClock():
    def __init__(self, hour, minute, second):
        # 布局
        self.centerX = 120  # 表盘中心坐标X
        self.centerY = 160  # 表盘中心坐标Y
        self.radius = 100  # 表盘圆半径

        # 表盘圆周坐标
        self.cirStart = self.getCoordinateList(1)
        self.cirEnd1 = self.getCoordinateList(1.05)
        self.cirEnd2 = self.getCoordinateList(1.10)

        # 时分秒指针头尾坐标
        self.hurTail = self.getCoordinateList(-0.1)
        self.hurHand = self.getCoordinateList(0.3)
        self.minTail = self.getCoordinateList(-0.1)
        self.minHand = self.getCoordinateList(0.5)
        self.secTail = self.getCoordinateList(-0.1)
        self.secHand = self.getCoordinateList(0.7)

        # 根据当前时间计算走过的秒数
        self.totalSec = hour * 3600 + minute * 60 + second

        self.drawClock()

    # 获取圆周上的60个坐标
    def getCoordinateList(self, mul):
        coordinateList = []
        # 0-15
        for n in range(15):
            x = int(self.centerX + self.radius * mul * math.cos(math.pi / 30 * (15 - n)))
            y = int(self.centerY - self.radius * mul * math.sin(math.pi / 30 * (15 - n)))
            coordinate = (x, y)
            coordinateList.append(coordinate)
        # 15-60
        for n in range(45):
            x = int(self.centerX + self.radius * mul * math.cos(math.pi / 30 * (60 - n)))
            y = int(self.centerY - self.radius * mul * math.sin(math.pi / 30 * (60 - n)))
            coordinate = (x, y)
            coordinateList.append(coordinate)
        return coordinateList

    # 画表盘
    def drawClock(self):
        screen.clear()
        # 画表盘
        for i in range(60):
            if i % 5 == 0:
                # 画时刻度 长线
                screen.drawline(self.cirStart[i][0], self.cirStart[i][1], self.cirEnd2[i][0], self.cirEnd2[i][1], 3, 0x000000)
            else:
                # 画秒刻度 短线
                screen.drawline(self.cirStart[i][0], self.cirStart[i][1], self.cirEnd1[i][0], self.cirEnd1[i][1], 2, 0x000000)

    # 开始运行
    def start(self):
        while True:
            start = time.ticks_ms()  # 记录开始时间

            # 获取列表下标
            hi = int(self.totalSec / 720)
            mi = int(self.totalSec / 60) % 60
            si = self.totalSec % 60

            # 画时分秒针并保留一段时间
            screen.drawline(self.hurTail[hi][0], self.hurTail[hi][1], self.hurHand[hi][0], self.hurHand[hi][1], 2, 0x000000)
            screen.drawline(self.minTail[mi][0], self.minTail[mi][1], self.minHand[mi][0], self.minHand[mi][1], 2, 0x000000)
            screen.drawline(self.secTail[si][0], self.secTail[si][1], self.secHand[si][0], self.secHand[si][1], 2, 0x000000)
            time.sleep_ms(980)  # 程序执行延时大约20ms

            # 擦除时分秒针
            screen.drawline(self.secTail[si][0], self.secTail[si][1], self.secHand[si][0], self.secHand[si][1], 2, 0xffffff)
            if self.totalSec % 60 == 59:
                screen.drawline(self.minTail[mi][0], self.minTail[mi][1], self.minHand[mi][0], self.minHand[mi][1], 2, 0xffffff)
            if self.totalSec % 720 == 719:
                screen.drawline(self.hurTail[hi][0], self.hurTail[hi][1], self.hurHand[hi][0], self.hurHand[hi][1], 2, 0xffffff)

            self.totalSec = self.totalSec + 1
            if self.totalSec >= 43200:
                self.totalSec = 0

            print(time.ticks_diff(time.ticks_ms(), start))  # 每一次循环运行时间


if __name__ == '__main__':
    cl = AnalogClock(1, 20, 0)  # 设置时间为1:20:00
    cl.start()

