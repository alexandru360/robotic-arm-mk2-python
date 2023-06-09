import time
from pcf8591_buttons import PCF8591
from pca9685_servo import PCA9685Servo

if __name__ == "__main__":
    try:
        _channel = 1
        _speed = 50

        pcf8591 = PCF8591()

        motor = PCA9685Servo(speed=_speed, channel=_channel)
        base = PCA9685Servo(speed=_speed, channel=0)

        while True:
            x = pcf8591.read_AIN0()
            y = pcf8591.read_AIN1()
            sw = pcf8591.read_AIN3()

            swRange = range(0, 5)
            swState = "pressed" if sw in swRange else "not pressed"

            xyTotal = x+y

            if sw in swRange:
                _channel = _channel + 1
                if _channel not in range(0, 3):
                    _channel = 1

            if xyTotal in range(200, 230):  # up
                print("Moving Up")
                motor.moveUpStep()

            if xyTotal in range(450, 470):  # down
                print("Moving Down")
                motor.moveDownStep()

            if xyTotal in range(400, 430):  # left
                print("Moving left")
                base.moveUpStep()

            if xyTotal in range(160, 180):  # right
                print("Moving right")
                base.moveDownStep()

            print(f"X: {x}, Y: {y}, Sw-state: {sw}-{swState}, Selected channel {_channel} xyTotal {xyTotal}")
            time.sleep(0.2)

    except KeyboardInterrupt:
        motor.stop()
        pass
