from src.pca9685_servo import PCA9685Servo
import time

if __name__ == "__main__":
    _channel = 0
    _speed = 50

    # Use I2C bus 1
    motor = PCA9685Servo(speed=_speed, channel=_channel)
    
    # motor.stopAndReset()
    motor.stop()