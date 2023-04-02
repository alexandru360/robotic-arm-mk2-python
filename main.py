import time
from src.buttons_pcf8591 import PCF8591
from src.pca9685_servo import MotorController

if __name__ == "__main__":
    _channel = 3
    _speed = 50

    # Use I2C bus 1
    motor = MotorController(speed=_speed, channel=_channel)

    pcf8591 = PCF8591()
    try:
        while True:
            xCoord = pcf8591.read_AIN0()
            yCoord = pcf8591.read_AIN1()

            print(f"X: {xCoord}, Y: {yCoord}")

            sw_state = pcf8591.read_SW()
            if sw_state == 0:
                print("Button pressed")
            else:
                print("Button not pressed")

            print(f"X: {xCoord}, Y: {yCoord}, Sw-state: {sw_state}")

            time.sleep(1)

    except KeyboardInterrupt:
        motor.stop()
        pass
