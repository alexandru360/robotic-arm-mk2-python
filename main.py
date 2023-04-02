import time
from src.pcf8591_buttons import PCF8591
from src.pca9685_servo import PCA9685Servo

if __name__ == "__main__":
    _channel = 3
    _speed = 50

    # Use I2C bus 1
    motor = PCA9685Servo(speed=_speed, channel=_channel)

    pcf8591 = PCF8591()
    try:
        while True:
            xCoord = pcf8591.read_AIN0()
            yCoord = pcf8591.read_AIN1()
            sw_state = pcf8591.read_AIN3()
            string = "Button pressed" if sw_state == 0 or sw_state == 1 else "Button not pressed"

            print(f"X: {xCoord}, Y: {yCoord}, Sw-state: {sw_state}-{string}")

            time.sleep(1)

    except KeyboardInterrupt:
        motor.stop()
        pass
