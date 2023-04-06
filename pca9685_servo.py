# servo_pca9685.py

import board
import busio

from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from motor_store import MotorStore

_lowAngle = 0
_halfAngle = 90.0
_maxAngle = 180.0

motorStore = MotorStore()

class PCA9685Servo:
    def __init__(self, speed, channel):
        self.speed = speed
        self.channel = channel

        # Initialize I2C bus
        i2c_bus = busio.I2C(board.SCL, board.SDA)

        # Initialize PCA9685 module
        self.pca9685 = PCA9685(i2c_bus)

        # Set the PWM frequency for the PCA9685 module
        self.pca9685.frequency = 50

        # Initialize the servo on the specified channel
        self.motor = servo.Servo(
            self.pca9685.channels[self.channel], min_pulse=500, max_pulse=2500)

    def setToOrigin(self):
        print(f"Motor on channel {self.channel} setting to its origin")
        motorStore.set_angle(self.channel, _lowAngle)
        self.motor.angle = _lowAngle

    def setToHalfAngle(self):
        print(f"Motor on channel {self.channel} setting to 90")
        motorStore.set_angle(self.channel, _halfAngle)
        self.motor.angle = _halfAngle

    def setToMaxAngle(self):
        print(f"Motor on channel {self.channel} setting to 180")
        motorStore.set_angle(self.channel, _maxAngle)
        self.motor.angle = _maxAngle

    def moveUp(self, increment=1):
        print(f"Motor on channel {self.channel} is moving up with angle increment {increment}")
        for angle in range(_lowAngle, float(_maxAngle) + 1, increment):
            self.motor.angle = float(angle)

    def moveDown(self, increment=1):
        print(
            f"Motor on channel {self.channel} is moving down with angle increment {increment}")
        for angle in range(float(_maxAngle), -1, -increment):
            self.motor.angle = float(angle)

    def sweep(self):
        print(
            f"Sweeping motor on channel {self.channel} through its full range of motion.")
        for angle in range(_lowAngle, float(_maxAngle) + 1, 5):
            self.motor.angle = float(angle)
        for angle in range(float(_maxAngle), -1, -5):
            self.motor.angle = float(angle)

    def stopAndReset(self):
        print(f"Stopping motor on channel {self.channel} and resetting to origin")
        motorStore.set_angle(self.channel, _lowAngle)
        self.motor.angle = _lowAngle

    def stop(self):
        motorStore.set_angle(self.channel, _maxAngle)
        self.motor.angle = _maxAngle

    def moveUpStep(self, increment=1):
        angle = float(motorStore.get_angle(self.channel) + 1)
        print(f"Incremented angle {angle}, increment received {increment}")
        if angle >= _lowAngle and angle <= _maxAngle:
            self.motor.angle = angle
            motorStore.set_angle(self.channel, angle)
        else:
            self.setToOrigin()

        print(f"New current angle {angle}")

    def moveDownStep(self, increment=1):
        angle = float(motorStore.get_angle(self.channel) - 1)
        print(f"Incremented angle {angle}, increment received {increment}")
        if angle >= _lowAngle and angle <= _maxAngle:
            self.motor.angle = angle
            motorStore.set_angle(self.channel, angle)
        else:
            self.setToOrigin()

        print(f"New current angle {angle}")
