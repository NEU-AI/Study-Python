from pyb import UART


class SPO2:
    def __init__(self, uart):
        self.uart = uart

    def fill(self, sData):
        l = len(sData)
        lData = '0' * (8 - l) + sData
        return lData

    def binToInt(self, bData):
        iData = 0
        for i in range(len(bData)):
            if (bData[-(i + 1)] == '1'):
                iData = iData + 2 ** i
        return iData

    def receiveData(self):
        while True:
            byte1 = self.uart.readchar()
            if byte1 >= 128:
                byte2 = self.uart.readchar()
                byte3 = self.uart.readchar()
                byte4 = self.uart.readchar()
                byte5 = self.uart.readchar()
                if byte2<128 and byte3<128 and byte4<128 and byte5<128:
                    dataList = ['', '', '', '', '']
                    dataList[0] = self.fill(bin(byte1)[2:])
                    dataList[1] = self.fill(bin(byte2)[2:])
                    dataList[2] = self.fill(bin(byte3)[2:])
                    dataList[3] = self.fill(bin(byte4)[2:])
                    dataList[4] = self.fill(bin(byte5)[2:])
                    return dataList

    def getSpList(self):
        dataList = self.receiveData()
        spList = []

        if (dataList[0][-7] == '1'):
            print("Pulse rate sound is on")

        if (dataList[0][-5] == '1'):
            print("Too long time in searching")
        elif (dataList[0][-6] == '1'):
            print("Oxygen saturation is getting lower")
        elif (dataList[2][-5] == '1'):
            print("Probe has something wrong")
        elif (dataList[2][-6] == '1'):
            print("Detecting pulse rate")
        else:
            print("Succeed to get data")
            signalStrength = self.binToInt(dataList[0][-4:])
            volumeGraph = self.binToInt(dataList[1][-7:])
            barGraph = self.binToInt(dataList[2][-4:])
            pulseRate = self.binToInt(dataList[2][-7] + dataList[3][-7:])
            spO2 = self.binToInt(dataList[4][-7:])
            spList.append(signalStrength)
            spList.append(volumeGraph)
            spList.append(barGraph)
            spList.append(pulseRate)
            spList.append(spO2)
        return spList

    def sleep(self, time):
        count = time * 300
        for i in range(count):
            self.uart.readchar()


if __name__ == '__main__':
    uart6 = UART(6, baudrate=4800, bits=8, parity=1, stop=1)
    sp = SPO2(uart6)
    while True:
        spList = sp.getSpList()
        if len(spList) != 0:
            print('PulseRate: ' + str(spList[3]))
            print('BloodOxygen: ' + str(spList[4]))
        sp.sleep(2)
