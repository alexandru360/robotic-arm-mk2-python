# buttons_pcf8591.py

import board
import busio

class PCF8591:
    def __init__(self, address=0x48, bus_number=1):
        self.address = address
        self.bus = busio.I2C(getattr(board, f"SCL_{bus_number}"), getattr(board, f"SDA_{bus_number}"))

    def read(self, channel):
        assert 0 <= channel <= 3, "Channel must be between 0 and 3 (inclusive)"
        self.bus.writeto(self.address, bytes([channel]))
        self.bus.readfrom_into(self.address, 1)  # Discard the first byte (dummy read)
        result = bytearray(1)
        self.bus.readfrom_into(self.address, result)
        return result[0]

    def read_AIN0(self):
        return self.read(0)

    def read_AIN1(self):
        return self.read(1)

    def read_AIN2(self):
        return self.read(2)

# Example usage
if __name__ == "__main__":
    pcf8591 = PCF8591()

    ain0_value = pcf8591.read_AIN0()
    ain1_value = pcf8591.read_AIN1()
    ain2_value = pcf8591.read_AIN2()

    print(f"AIN0: {ain0_value}, AIN1: {ain1_value}, AIN2: {ain2_value}")
