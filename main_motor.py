import time
from src.pcf8591_buttons import PCF8591
from src.pca9685_servo import PCA9685Servo

if __name__ == "__main__":
    try:
        _channel = 2
        _speed = 50

        # Use I2C bus 1
        motor = PCA9685Servo(speed=_speed, channel=_channel)

        motor.moveUpStep()

        # motor.moveDownStep()

        time.sleep(1)

    except KeyboardInterrupt:
        # motor.stop()
        pass
