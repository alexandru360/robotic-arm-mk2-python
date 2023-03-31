# main.py

import time
from buttons_pcf8591 import PCF8591
from adafruit_pca9685 import PCA9685

pca9685 = PCA9685(i2c_bus_number=1)  # Use I2C bus 1
pcf8591 = PCF8591(bus_number=1)  # Use I2C bus 1

SERVO_MIN = 150  # Min pulse length out of 4096
SERVO_MAX = 600  # Max pulse length out of 4096

# Set channels 0 through 7 to the "neutral" signal (375 out of 4096)
for i in range(8):
    pca9685.channels[i].duty_cycle = 0x6FFF

def set_servo_angle(channel, angle):
    duty_cycle = int((angle / 180) * (SERVO_MAX - SERVO_MIN) + SERVO_MIN)
    pca9685.channels[channel].duty_cycle = duty_cycle

try:
    while True:
        ain0_value = pcf8591.read_AIN0()
        ain1_value = pcf8591.read_AIN1()
        ain2_value = pcf8591.read_AIN2()

        print(f"AIN0: {ain0_value}, AIN1: {ain1_value}, AIN2: {ain2_value}")

        # Map analog values to servo angles
        servo_1_angle = int(ain0_value / 255 * 180)
        servo_2_angle = int(ain1_value / 255 * 180)
        servo_3_angle = int(ain2_value / 255 * 180)

        # Set servo angles
        set_servo_angle(0, servo_1_angle)
        set_servo_angle(1, servo_2_angle)
        set_servo_angle(2, servo_3_angle)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping motors")
    for i in range(8):
        pca9685.channels[i].duty_cycle = 0x0000
