import time

from buttons_pcf8591 import PCF8591

if __name__ == "__main__":
    pcf8591 = PCF8591()

    ain0_value = pcf8591.read_AIN0()
    ain1_value = pcf8591.read_AIN1()
    ain2_value = pcf8591.read_AIN2()

    print(f"AIN0: {ain0_value}, AIN1: {ain1_value}, AIN2: {ain2_value}")

    time.sleep(1)   