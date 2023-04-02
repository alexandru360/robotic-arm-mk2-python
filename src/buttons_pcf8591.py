# buttons_pcf8591.py

from board import SCL, SDA
import busio

class PCF8591:
    def __init__(self, address=0x48):
        self.address = address
        self.bus = busio.I2C(SCL, SDA) # thi si true if the i2c is on the default RPI i2c-1
        
    def read(self, channel):
        assert 0 <= channel <= 3, "Channel must be between 0 and 3 (inclusive)"
        self.bus.writeto(self.address, bytes([channel]))
        self.bus.readfrom_into(self.address, bytearray(1))  # Discard the first byte (dummy read)
        result = bytearray(1)
        self.bus.readfrom_into(self.address, result)
        return result[0]

    def read_AIN0(self):
        return self.read(0)

    def read_AIN1(self):
        return self.read(1)

    # def read_AIN2(self):
    #     return self.read(2)

    # def read_AIN3(self):
    #     return self.read(3)

    def read_SW(self):
        return self.read(3)

