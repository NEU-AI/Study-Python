import time
from pyb import UART


class MHZ14A:
    READ_COM = [0xff, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79]
    CALIBRATE_COM = [0xff, 0x01, 0x87, 0x00, 0x00, 0x00, 0x00, 0x00, 0x78]

    def __init__(self, uart):
        self.uart = uart
        time.sleep(2)
        self.calibrate()

    def calibrate(self):
        self.uart.write(bytearray(MHZ14A.CALIBRATE_COM))

    def getConcentration(self):
        self.uart.write(bytearray(MHZ14A.READ_COM))
        res = self.uart.read(9)
        checksum = 0xff & (~(res[1] + res[2] + res[3] + res[4] + res[5] + res[6] + res[7]) + 1)
        co2PPM = (res[2] << 8) | res[3]
        if res[8] == checksum:
            print("succeed to get concentration of CO2")
            return co2PPM
        else:
            print("error in received data")
            return -1


if __name__ == '__main__':
    uart6 = UART(6, baudrate=9600, bits=8, parity=None, stop=1)
    co2 = MHZ14A(uart6)
    while True:
        concentration = co2.getConcentration()
        print(concentration)
        time.sleep(1)
