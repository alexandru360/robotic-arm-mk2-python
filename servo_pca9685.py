# servo_pca9685.py

import time
import board
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

class MotorController:
      def __init__(self, address=0x40, bus_number=1):
        self.bus = busio.I2C(SCL, SDA)
        self.pca = PCA9685(self.bus, address=address)
        self.pca.frequency = 50  # Set the frequency to 50 Hz
        self.servos = [Servo(self.pca, channel) for channel in range(16)]
        
        # Initialize I2C bus
        i2c_bus = busio.I2C(board.SCL, board.SDA)
        
        # Initialize PCA9685 module
        self.pca9685 = PCA9685(i2c_bus)
        
        # Set the PWM frequency for the PCA9685 module
        self.pca9685.frequency = 50

        # Initialize the servo on the specified channel
        self.motor = servo.Servo(self.pca9685.channels[self.channel])

    def moveUp(self, increment=1):
        print(f"Motor on channel {self.channel} is moving up with angle increment {increment}")
        for angle in range(0, 181, increment):
            self.motor.angle = angle
            time.sleep(0.1)

    def moveDown(self, increment=1):
        print(f"Motor on channel {self.channel} is moving down with angle increment {increment}")
        for angle in range(180, -1, -increment):
            self.motor.angle = angle
            time.sleep(0.1)

    def sweep(self):
        print(f"Sweeping motor on channel {self.channel} through its full range of motion.")
        for angle in range(0, 181, 5):
            self.motor.angle = angle
            time.sleep(0.1)
        for angle in range(180, -1, -5):
            self.motor.angle = angle
            time.sleep(0.1)

    def stop(self):
        print(f"Stopping motor on channel {self.channel}")
        self.motor.angle = 90
