import time
from pyb import Pin, ADC


class ZZSGTHC:
    def __init__(self, adcPin):
        self.adc = ADC(Pin(adcPin))

    def getSoilMoisture(self):
        voltage = self.adc.read()
        moisture = voltage * 2 / 100
        return round(moisture, 2)


if __name__ == '__main__':
    soil = ZZSGTHC('Y11')
    while True:
        moisture = soil.getSoilMoisture()
        print(moisture)
        time.sleep(1)
