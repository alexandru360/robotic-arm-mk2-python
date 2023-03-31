# main.py

from buttons_pcf8591 import PCF8591
from servo_pca9685 import MotorController
import time

if __name__ == "__main__":
    motor = MotorController(speed=100, channel=0, bus_number=1)  # Use I2C bus 1

    # Move the motor up and down with a specific angle increment
    motor.moveUp(increment=1)
    # motor.moveDown(increment=5)

    # Uncomment the following line if you want to add the stop method to the MotorController class
    # motor.stop()

    # Wait for the motor to complete its movement before reading the values
    time.sleep(1)

    # Create an instance of the PCF8591 class and use its methods
    pcf8591 = PCF8591()

    ain0_value = pcf8591.read_AIN0()
    ain1_value = pcf8591.read_AIN1()
    ain2_value = pcf8591.read_AIN2()

    print(f"AIN0: {ain0_value}, AIN1: {ain1_value}, AIN2: {ain2_value}")
