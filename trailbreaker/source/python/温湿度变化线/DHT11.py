from pyb import Pin
import time, dht


class DHT11:
    def __init__(self, dataPin):
        self.dht = dht.DHT11(Pin(dataPin))

    def getData(self):
        dataList = []
        try:
            self.dht.measure()
            print("succeed to get data")
        except:
            print("error in connection")
            return dataList
        
        humidity = self.dht.humidity()
        temperature = self.dht.temperature()
        dataList.append(round(humidity, 2))
        dataList.append(round(temperature, 2))
        return dataList


if __name__ == '__main__':
    DHT11_sensor = DHT11('Y4')
    while True:
        dhList = DHT11_sensor.getData()
        if dhList == []:
            continue
        else:
            print('humidity: ' + str(dhList[0]) + '％RH')
            print('temperature: ' + str(dhList[1]) + '℃')
            print()
        time.sleep(1)
