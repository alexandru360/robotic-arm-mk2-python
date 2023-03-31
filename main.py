from servo_pca9685 import MotorController
import time

if __name__ == "__main__":
    # motor = MotorController(speed=100, channel=0, bus_number=1)  # Use I2C bus 1

    # motor.moveUp(increment=1)
    # time.sleep(1)
    
    # motor.stop()

    motor1 = MotorController(speed=100, channel=1, bus_number=1)  # Use I2C bus 1

    motor1.moveUp(increment=1)
    time.sleep(1)
    
    motor1.stop()

    # time.sleep(1)
