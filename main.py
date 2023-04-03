import time
from src.pcf8591_buttons import PCF8591
from src.pca9685_servo import PCA9685Servo

if __name__ == "__main__":
    try:
        _channel = 1
        _speed = 50

        # Use I2C bus 1
        motor = PCA9685Servo(speed=_speed, channel=_channel)

        pcf8591 = PCF8591()

        while True:
            x = pcf8591.read_AIN0()
            y = pcf8591.read_AIN1()
            sw = pcf8591.read_AIN3()
            swState = "pressed" if sw == 0 or sw == 1 else "not pressed"

            if sw in range(0, 1):
                _channel = _channel + 1
                if _channel not in range(0, 3):
                    _channel = 1

            if x in range(155, 160) and y in range(203, 206):  # up
                print("Moving Up")
                motor.moveUp()

            if x in range(253, 256) and y in range(203, 206):  # down
                print("Moving Down")
                motor.moveUp()

            # The only channel of left and right
            if x in range(163, 167) and y in range(253, 256):  # left
                # Use I2C bus 1
                print("Moving left")

                motor = PCA9685Servo(speed=_speed, channel=0)
                motor.moveUp()

            if x in range(163, 167) and y in range(0, 5):  # right
                # Use I2C bus 1
                print("Moving right")

                motor = PCA9685Servo(speed=_speed, channel=0)
                motor.moveDown()

            print(
                f"X: {x}, Y: {y}, Sw-state: {sw}-{swState}, Selected channel {_channel}")

            time.sleep(1)

    except KeyboardInterrupt:
        motor.stop()
        pass
